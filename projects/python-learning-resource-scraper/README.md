# 🐍 Python Learning Resource Scraper

Python Learning Resource Scraper is an intermediate Python portfolio project inspired by the Towards AI **Web Scraping** lesson. Instead of copying the lesson's example, it builds a small learning-resource application that collects useful details from three official Python documentation pages.

## 🎯 Project Overview

The program fetches a predefined list of Python documentation pages, parses their HTML, and reports each page's title, first main heading, URL, and HTTP status code. The three requests run concurrently with threads, while the final results remain in the same order as the input URLs.

The project deliberately scrapes only these three public pages. It does not crawl the whole Python documentation site or follow links.

## ✨ Features

- Scrapes three fixed official Python documentation URLs
- Uses `requests` to fetch HTML
- Uses BeautifulSoup to extract page titles and the first `<h1>` heading
- Runs one worker thread per page
- Preserves the original URL order in the final summary
- Handles request failures and missing HTML elements gracefully
- Uses a ten-second request timeout
- Includes a small verbose diagnostic mode

## 🐍 Python Concepts

- `requests` and HTTP response data
- BeautifulSoup HTML parsing
- Functions, parameters, arguments, and return values
- Default arguments with `verbose=False`
- A readable `lambda` function for title extraction
- LEGB scope with a global variable and nested helper function
- `threading.Thread`, `.start()`, and `.join()`
- Lists, dictionaries, loops, `enumerate()`, and f-strings
- `try` / `except requests.RequestException`
- The `if __name__ == "__main__":` execution guard

## 🧩 How It Works

`run_scraper()` defines the three documentation URLs and creates a `[None, None, None]` results list. Each thread calls `update_results()`, which calls `scrape_resource()` and stores its dictionary at the matching list index. This indexed storage preserves input order even when requests finish at different times.

Inside `scrape_resource()`, `requests.get()` retrieves the page with a timeout. BeautifulSoup parses `response.text`; a small lambda extracts the title, and `soup.find("h1")` finds the first heading. A request exception returns a useful fallback dictionary instead of stopping the whole program.

## 📁 Project Structure

```text
python-learning-resource-scraper/
├── README.md
├── python_learning_resource_scraper.py
├── python_learning_resource_scraper.ipynb
└── requirements.txt
```

- `python_learning_resource_scraper.py` contains the local Python script.
- `python_learning_resource_scraper.ipynb` presents the project for Jupyter or Google Colab.
- `README.md` documents the project.
- `requirements.txt` lists the two third-party packages used by the scraper.

## 🚀 Running Locally

Python 3 is required. From this project directory, install the dependencies and run:

```bash
pip install -r requirements.txt
python python_learning_resource_scraper.py
```

You can also use `python3` in place of `python`.

## 🌐 Google Colab

Open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/python-learning-resource-scraper/python_learning_resource_scraper.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 💡 Example Output

```text
=== Python Learning Resource Scraper ===
Fetching three official Python documentation pages...

=== Python Learning Resources ===

1. The Python Tutorial
   Heading: The Python Tutorial
   Status: 200
   URL: https://docs.python.org/3/tutorial/

2. The Python Standard Library
   Heading: The Python Standard Library
   Status: 200
   URL: https://docs.python.org/3/library/

3. Introduction — Python 3.14.0 documentation
   Heading: Introduction
   Status: 200
   URL: https://docs.python.org/3/reference/introduction.html
```

Exact titles can change when the Python documentation version changes.

## 📚 What I Learned

This project practices sending HTTP requests, parsing returned HTML, extracting specific elements, and storing related values in dictionaries. It also connects default arguments, lambda functions, nested scope, exception handling, and basic threading in one small application.

## 📝 Notes / Responsible Scraping

- The scraper uses a small fixed set of public pages and does not recursively crawl links.
- Responsible scraping means respecting site rules and robots guidance and avoiding excessive requests.
- This project does not attempt to bypass restrictions, use authentication, or evade anti-bot systems.
- Network results and documentation titles may change over time.
- `threading` is part of Python's standard library and is not listed in `requirements.txt`.
