# 📰 News Insight Analyzer

News Insight Analyzer is an intermediate Python portfolio project inspired by the Towards AI **News Analyzer: Summarize, Sentiment, and Tags** lesson. It uses Google's Gemini API to analyze pasted news article text and presents the result in a small Gradio web application.

## 🎯 Project Overview

The application asks Gemini to return a concise summary, one sentiment label, three to five relevant tags, and one key takeaway. The key takeaway is a small original enhancement beyond the lesson. Gemini's response is requested as JSON and parsed with Python's standard-library `json` module.

## ✨ Features

- 2-3 sentence article summary
- `positive`, `negative`, or `neutral` sentiment
- Three to five relevant lowercase tags
- One-sentence key takeaway
- JSON response parsing with `json.loads()`
- Simple validation and friendly error messages
- Gradio `Blocks` interface
- Gemini API key loaded from `GEMINI_API_KEY`

## 🐍 Python Concepts

- The `google-genai` SDK
- Environment variables for API keys
- Functions, parameters, and return values
- Strings and f-strings for prompt construction
- Dictionaries and lists
- JSON parsing with `json.loads()`
- `.get()` with fallback values
- `try` / `except` error handling
- `if __name__ == "__main__":`

## 🧩 How It Works

`analyze_news_article()` builds a readable prompt and sends it to Gemini with the current Google GenAI SDK. The response text is parsed into a Python dictionary, then the four requested fields are extracted and checked. Tags remain a Python list internally; `format_tags()` converts that list into display text for Gradio.

If the article is empty, Gemini returns invalid JSON, the sentiment is unexpected, or an API error occurs, the application returns beginner-friendly fallback messages instead of a traceback.

## 📁 Project Structure

```text
news-insight-analyzer/
├── README.md
├── news_insight_analyzer.py
├── news_insight_analyzer.ipynb
└── requirements.txt
```

- `news_insight_analyzer.py` contains the primary local application.
- `news_insight_analyzer.ipynb` presents the project for Jupyter or Google Colab.
- `README.md` documents the project.
- `requirements.txt` lists the Gemini SDK and Gradio dependencies.

## 🚀 Setup and Running Locally

Python 3 is required. From this project directory, create and activate a virtual environment:

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
python news_insight_analyzer.py
```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY"
python news_insight_analyzer.py
```

Open the local Gradio address shown in the terminal.

## 🌐 Google Colab

Open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/news-insight-analyzer/news_insight_analyzer.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Before running the analysis, add a secret named `GEMINI_API_KEY` in Colab's Secrets panel and enable notebook access. The notebook retrieves the secret at runtime; you should not type your key into a visible code cell.

Gemini offers a free tier, which makes it convenient for learners and testers using their own Gemini API key. Every user must supply their own key; no API key is included in this repository. Gemini availability, free-tier limits, quotas, and pricing are controlled by Google and may change over time.

## 💡 Example Output

```text
Summary: The city approved a new clean-energy plan after months of discussion. The plan will fund solar projects and update building standards over the next five years.
Sentiment: positive
Tags: climate, energy, policy, cities
Key Takeaway: The city has committed to a five-year clean-energy program.
```

The exact output depends on the article and Gemini response.

## 📚 What I Learned

This project practices calling a current generative AI SDK, keeping credentials outside source code, designing a focused prompt, parsing JSON, validating returned values, and connecting Python functions to Gradio outputs.

## 📝 Notes

- Gemini output can vary, so the application uses simple fallbacks for missing or invalid values.
- Sentiment describes the tone of the supplied article or text; it is not an objective judgment of whether the underlying real-world event is positive or negative.
- This project is for learning and does not verify the accuracy of an article or its analysis.
- API usage may have rate limits or costs according to the user's Google AI Studio account.
- The notebook is a learning companion; `news_insight_analyzer.py` is the primary local application.
