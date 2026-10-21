# 🚀 NASA Space RAG

NASA Space RAG is a beginner-friendly retrieval-augmented generation (RAG) application inspired by the TowardsAI **Chat with Your Documents: A RAG Application** lesson. It uses five NASA-derived text documents, Gemini, and Gradio to answer questions from retrieved source text.

## 🎯 Project Overview

The application embeds each NASA document and saves the documents and embeddings in a JSON cache. For each question, it creates a question embedding, calculates cosine similarity against the document embeddings, and retrieves the two most similar documents. Gemini then receives those documents as context and is instructed to answer using only that text.

## ✨ Features

- Five included NASA-derived reference documents
- Gemini document and question embeddings with `gemini-embedding-2`
- JSON cache for reusing document embeddings
- Manual cosine similarity calculation
- Top-two document retrieval with actual similarity scores
- Grounded answer generation with `gemini-3.5-flash-lite`
- Fallback response when the documents do not support an answer
- Gradio `Blocks` interface for questions, answers, document names, and scores
- API key loaded from the `GEMINI_API_KEY` environment variable or Google Colab Secrets

## 🐍 Python Concepts

- Classes, objects, and methods
- Functions, parameters, return values, and `if` / `else` control flow
- Lists and dictionaries for documents and embeddings
- JSON reading and writing with the standard-library `json` module
- File and folder handling with `os`
- Manual vector comparison with `math.sqrt()`, `sum()`, and `zip()`
- Sorting scored documents with a `lambda` function
- Gemini API calls with the Google GenAI SDK
- Gradio components and button event handlers

## 🧩 How It Works

`SpaceAssistant` stores the NASA documents, their embeddings, and the Gemini client. `embed_documents()` creates one embedding per document. `save_embeddings()` writes the aligned documents and vectors to `doc_embeddings.json`, and `load_embeddings()` reuses a valid cache with the expected embedding model.

For a question, `answer_question()` embeds the text and calls `retrieve_documents()`. Retrieval calculates cosine similarity between the question vector and each document vector, sorts by score, and returns the top two. The prompt includes their contents and instructs Gemini to answer only from them. If the provided documents do not support an answer, the requested fallback is: `I can't find the answer in the NASA documents.`

## 🌌 NASA Document Sources

- [NASA Science — Mars Facts](https://science.nasa.gov/mars/facts/) — `mars.txt`
- [NASA Science — Moon Phases](https://science.nasa.gov/moon/moon-phases/) — `moon.txt`
- [NASA Science — Solar System Facts](https://science.nasa.gov/solar-system/solar-system-facts/) — `solar_system.txt`
- [NASA — Space Station Research and Technology](https://www.nasa.gov/international-space-station/space-station-research-and-technology/) — `international_space_station.txt`
- [NASA Science — Black Holes](https://science.nasa.gov/universe/black-holes/) — `black_holes.txt`

## 📁 Project Structure

```text
nasa-space-rag/
├── README.md
├── nasa_space_rag.py
├── nasa_space_rag.ipynb
├── requirements.txt
└── documents/
    ├── black_holes.txt
    ├── international_space_station.txt
    ├── mars.txt
    ├── moon.txt
    └── solar_system.txt
```

- `nasa_space_rag.py` contains the primary local application.
- `nasa_space_rag.ipynb` presents the project for Jupyter and Google Colab.
- `documents/` contains the five NASA-derived text files used for retrieval.
- `requirements.txt` lists the Google GenAI SDK and Gradio dependencies.

## 🚀 Setup and Running Locally

Use Python 3.10 or newer. From this project directory, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```text
.venv\\Scripts\\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Set your own Gemini API key as an environment variable. Never place the key in the Python file, notebook, README, or a committed `.env` file.

macOS / Linux:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
python nasa_space_rag.py
```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY"
python nasa_space_rag.py
```

Open the local Gradio address shown in the terminal. The application uses `gemini-embedding-2` for document and question embeddings and `gemini-3.5-flash-lite` for answer generation.

## 🌐 Google Colab

Open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/nasa-space-rag/nasa_space_rag.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Before running the notebook, add a secret named `GEMINI_API_KEY` in Colab's Secrets panel and enable notebook access. The notebook retrieves the secret at runtime without displaying it. It installs `google-genai` and `gradio`, downloads the five text files from this public repository, and launches the Gradio interface. The JSON cache is stored in the current Colab runtime and may be lost when that runtime resets.

The Gradio share link is temporary and is available while the notebook cell is running. Stop the cell when you finish using the interface.

## 💡 Example Questions

```text
What are the phases of the Moon?
What is the International Space Station used for?
What is a black hole?
What are some facts about Mars?
How is the Solar System organized?
```

Questions outside the included documents should receive the fallback: `I can't find the answer in the NASA documents.` The exact answer and ranking may vary.

## 📊 Similarity Scores

The Gradio interface displays the filenames of the two retrieved documents and their actual cosine similarity scores, rounded to three decimal places. The scores are calculated by Python; they are not generated by Gemini and are not confidence scores. A higher score means the question embedding is more aligned with a document embedding, but does not guarantee that the document contains a complete answer.

## 📚 What I Learned

This project connects a Python class with API calls, embedding creation and caching, manual cosine similarity, document retrieval, and grounded answer generation. It also practices keeping an API key outside source files and connecting a Python method to a Gradio interface.

## 📝 Notes

- The application uses whole documents and does not split them into chunks.
- Answers are limited to information supported by the five included NASA-derived text files.
- A cached embedding file must be recreated if the source documents or embedding model changes.
- Gemini access, model availability, quotas, and usage limits are controlled by Google and may change.
- No API key is included in this repository; users provide their own key.
- The Colab notebook is a learning companion; `nasa_space_rag.py` is the primary local application.
