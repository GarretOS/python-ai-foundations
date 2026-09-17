import json

import gradio as gr
from google import genai


MODEL_NAME = "gemini-3.8-flash"


def build_prompt(article_text):
    return f'''Analyze the supplied news article.

Return valid JSON only. Do not use Markdown code fences, and do not add any
prefix or suffix text. Use only these keys: summary, sentiment, tags,
key_takeaway.

Requirements:
- summary must be a concise 2-3 sentence overview.
- sentiment must be exactly positive, negative, or neutral.
- tags must be 3-5 relevant lowercase keywords or topics as a JSON list.
- key_takeaway must be one concise sentence stating the most important point.

Example structure:
{{
  "summary": "A concise overview.",
  "sentiment": "neutral",
  "tags": ["technology", "policy", "research"],
  "key_takeaway": "The article's most important point."
}}

News article:
{article_text}'''


def fallback_result(message):
    return (
        message,
        "No sentiment found.",
        [],
        "No takeaway found.",
    )


def analyze_news_article(article_text):
    if not article_text or not article_text.strip():
        return fallback_result("Please paste a news article before analyzing it.")

    try:
        client = genai.Client()
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=build_prompt(article_text.strip()),
        )
        article_data = json.loads(response.text)

        summary = article_data.get("summary", "No summary found.")
        sentiment = article_data.get("sentiment", "No sentiment found.")
        tags = article_data.get("tags", [])
        key_takeaway = article_data.get("key_takeaway", "No takeaway found.")

        if sentiment not in {"positive", "negative", "neutral"}:
            sentiment = "No sentiment found."

        return summary, sentiment, tags, key_takeaway

    except json.JSONDecodeError:
        return fallback_result("Gemini returned text that was not valid JSON.")
    except Exception as error:
        print(f"News analysis failed: {error}")
        return fallback_result(
            "The article could not be analyzed. Check your Gemini API key and try again."
        )


def format_tags(tags):
    if tags:
        return ", ".join(tags)
    return "No tags found."


def gradio_interface(article_text):
    summary, sentiment, tags, key_takeaway = analyze_news_article(article_text)
    return summary, sentiment, format_tags(tags), key_takeaway


def build_news_analyzer_app():
    with gr.Blocks() as demo:
        gr.Markdown(
            "# 📰 News Insight Analyzer\n"
            "Paste a news article to get a summary, sentiment, tags, and key takeaway."
        )

        article_input = gr.Textbox(
            label="Paste your news article here",
            placeholder="Paste the full text of a news article...",
            lines=12,
        )
        analyze_button = gr.Button("Analyze Article")

        summary_output = gr.Textbox(label="Summary", lines=3)
        sentiment_output = gr.Textbox(label="Sentiment")
        tags_output = gr.Textbox(label="Tags")
        takeaway_output = gr.Textbox(label="Key Takeaway", lines=2)

        analyze_button.click(
            fn=gradio_interface,
            inputs=article_input,
            outputs=[
                summary_output,
                sentiment_output,
                tags_output,
                takeaway_output,
            ],
        )

    return demo


if __name__ == "__main__":
    demo = build_news_analyzer_app()
    demo.launch()
