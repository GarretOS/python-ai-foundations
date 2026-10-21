"""A simple NASA document RAG assistant using Google's Gemini API."""

import json
import math
import os

import gradio as gr
from google import genai


EMBEDDING_MODEL = "gemini-embedding-2"
GENERATION_MODEL = "gemini-3.5-flash-lite"
CACHE_FILENAME = "doc_embeddings.json"
NO_ANSWER = "I can't find the answer in the NASA documents."


class SpaceAssistant:
    """Manages NASA documents, embeddings, retrieval, and answers."""

    def __init__(self):
        self.documents = []
        self.embeddings = []
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key) if self.api_key else None

    def load_documents(self, documents_folder):
        """Load all text documents from the specified folder."""
        if not os.path.isdir(documents_folder):
            raise FileNotFoundError(f"Documents folder not found: {documents_folder}")

        self.documents = []
        for filename in sorted(os.listdir(documents_folder)):
            if filename.endswith(".txt"):
                filepath = os.path.join(documents_folder, filename)
                with open(filepath, "r", encoding="utf-8") as document_file:
                    content = document_file.read()

                self.documents.append({
                    "filename": filename,
                    "content": content,
                })

        if not self.documents:
            raise FileNotFoundError(f"No .txt documents found in {documents_folder}")

    def embed_documents(self):
        """Generate one Gemini embedding for each loaded document."""
        if not self.documents:
            raise ValueError("No documents are loaded.")
        if self.client is None:
            raise RuntimeError("GEMINI_API_KEY is not configured.")

        self.embeddings = []
        for document in self.documents:
            response = self.client.models.embed_content(
                model=EMBEDDING_MODEL,
                contents=document["content"],
            )
            self.embeddings.append(response.embeddings[0].values)

    def save_embeddings(self, cache_path):
        """Save documents and their aligned embeddings to a JSON cache."""
        if len(self.documents) != len(self.embeddings):
            raise ValueError("Documents and embeddings must have matching lengths.")

        cache = {
            "documents": self.documents,
            "embeddings": self.embeddings,
            "embedding_model": EMBEDDING_MODEL,
        }
        with open(cache_path, "w", encoding="utf-8") as cache_file:
            json.dump(cache, cache_file)

    def load_embeddings(self, cache_path):
        """Load documents and embeddings from the JSON cache."""
        try:
            with open(cache_path, "r", encoding="utf-8") as cache_file:
                cache = json.load(cache_file)

            documents = cache["documents"]
            embeddings = cache["embeddings"]
            if not isinstance(documents, list) or not isinstance(embeddings, list):
                raise ValueError("Cache documents and embeddings must be lists.")
            if len(documents) != len(embeddings) or not documents:
                raise ValueError("Cache documents and embeddings are not aligned.")
            if cache.get("embedding_model") not in (None, EMBEDDING_MODEL):
                raise ValueError("Cache uses a different embedding model.")

            self.documents = documents
            self.embeddings = embeddings
            return True
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Could not load embeddings cache: {error}")
            return False

    def cosine_similarity(self, vector_a, vector_b):
        """Calculate cosine similarity using only math, sum, and zip."""
        if len(vector_a) != len(vector_b):
            raise ValueError("Vectors must have the same length.")

        dot_product = sum(value_a * value_b for value_a, value_b in zip(vector_a, vector_b))
        magnitude_a = math.sqrt(sum(value * value for value in vector_a))
        magnitude_b = math.sqrt(sum(value * value for value in vector_b))
        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0
        return dot_product / (magnitude_a * magnitude_b)

    def retrieve_documents(self, question_embedding, top_k=2):
        """Return the highest-scoring documents with their real scores."""
        if len(self.documents) != len(self.embeddings):
            raise ValueError("Documents and embeddings are not aligned.")

        scored_documents = []
        for index, embedding in enumerate(self.embeddings):
            score = self.cosine_similarity(question_embedding, embedding)
            scored_documents.append({
                "filename": self.documents[index]["filename"],
                "content": self.documents[index]["content"],
                "score": score,
            })

        scored_documents.sort(key=lambda document: document["score"], reverse=True)
        return scored_documents[:top_k]

    def answer_question(self, question):
        """Retrieve supporting documents and generate a grounded Gemini answer."""
        if not question or not question.strip():
            return "Please enter a question.", "No documents retrieved."
        if not self.documents:
            return "No NASA documents are loaded.", "No documents retrieved."
        if len(self.documents) != len(self.embeddings):
            return "Embeddings are unavailable. Run the application with a valid Gemini API key.", "No documents retrieved."
        if self.client is None:
            return "Gemini API unavailable: GEMINI_API_KEY is not configured.", "No documents retrieved."

        try:
            question_response = self.client.models.embed_content(
                model=EMBEDDING_MODEL,
                contents=question.strip(),
            )
            question_embedding = question_response.embeddings[0].values
            retrieved_documents = self.retrieve_documents(question_embedding)
            context = "\n\n".join(
                f"Document: {document['filename']}\n{document['content']}"
                for document in retrieved_documents
            )
            prompt = f"""Answer the question using only the NASA documents below.
If the documents do not support an answer, say exactly: "{NO_ANSWER}"
Do not use outside knowledge.

Question: {question.strip()}

NASA documents:
{context}
"""
            answer_response = self.client.models.generate_content(
                model=GENERATION_MODEL,
                contents=prompt,
            )
            answer = answer_response.text
            retrieval_text = "\n".join(
                f"{document['filename']} — {document['score']:.3f}"
                for document in retrieved_documents
            )
            return answer, retrieval_text
        except Exception as error:
            return f"Gemini API error: {error}", "Retrieved documents were not sent as an answer."


def prepare_assistant():
    """Load the NASA documents and reuse the cache when it is available."""
    assistant = SpaceAssistant()
    project_folder = os.path.dirname(__file__)
    documents_folder = os.path.join(project_folder, "documents")
    cache_path = os.path.join(project_folder, CACHE_FILENAME)
    assistant.load_documents(documents_folder)

    if not assistant.load_embeddings(cache_path):
        if assistant.client is None:
            print("Embeddings were not generated because GEMINI_API_KEY is missing.")
        else:
            assistant.embed_documents()
            assistant.save_embeddings(cache_path)
    return assistant


def build_interface(assistant):
    """Build the simple Gradio Blocks interface."""
    with gr.Blocks(title="NASA Space RAG") as demo:
        gr.Markdown("# NASA Space RAG")
        question = gr.Textbox(label="Question", placeholder="Ask a question about NASA space topics...")
        ask_button = gr.Button("Ask")
        answer = gr.Textbox(label="Answer", lines=6)
        retrieved = gr.Textbox(label="Top two retrieved documents and cosine similarity", lines=3)
        ask_button.click(
            fn=assistant.answer_question,
            inputs=question,
            outputs=[answer, retrieved],
        )
    return demo


def main():
    try:
        assistant = prepare_assistant()
        print(f"Using embedding model: {EMBEDDING_MODEL}")
        print(f"Using generation model: {GENERATION_MODEL}")
        print(f"Loaded documents: {len(assistant.documents)}")
        build_interface(assistant).launch()
    except Exception as error:
        print(f"Could not start NASA Space RAG: {error}")


if __name__ == "__main__":
    main()
