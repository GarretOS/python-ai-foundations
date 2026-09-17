# 🐍 Python Foundations Quiz

Python Foundations Quiz is a beginner-friendly web quiz based on the Towards AI lesson **Interactive Quiz App with Gradio**. It uses Gradio to present simple Python questions, answer choices, and friendly feedback in a small browser-based application.

## 🎯 Project Overview

The quiz contains nine intentionally easy questions about Python fundamentals. `quiz_app.py` builds the Gradio interface, while `quiz_data.py` stores the questions as a local Python module. The notebook is a supplementary learning companion; the Python script is the primary executable application.

## ✨ Features

- Nine beginner-friendly Python questions
- Dropdown question selection
- Radio-button answer choices
- Friendly correct and incorrect feedback
- Short explanations after incorrect answers
- Clears the previous answer and feedback when a new question is selected
- Separate quiz data module
- Gradio `Blocks` interface and event handlers
- No advanced web framework or public share URL enabled by default

## 🐍 Python Concepts

- Lists and dictionaries
- List comprehensions
- `enumerate()` for question lookup
- `None` for a missing question result
- Functions, imports, and return values
- `if` / `else` control flow
- The `with` statement
- `if __name__ == "__main__":`

## 🧩 Gradio Concepts

- Third-party package installation with `pip`
- `gr.Blocks()` for the application layout
- `gr.Dropdown`, `gr.Textbox`, `gr.Radio`, and `gr.Button`
- `.change()` for updating a question and its choices
- `.click()` for checking an answer
- `demo.launch()` for running the local app

## 🧠 How It Works

`quiz_data.py` defines `QUIZ_QUESTIONS`, a list of dictionaries containing each question, its options, the correct answer, and a short explanation. `quiz_app.py` imports that constant and uses a list comprehension to create the dropdown labels.

When a question changes, `find_question_index()` uses `enumerate()` to locate the matching dictionary. `quiz_interface()` returns updated component configurations for the question text and options, resets the Radio value, and clears previous feedback. When the button is clicked, `check_answer()` looks up the same question and uses a clear `if` / `else` statement to return feedback.

## 📁 Project Structure

```text
python-foundations-quiz/
├── README.md
├── quiz_app.py
├── quiz_data.py
├── python_foundations_quiz.ipynb
└── requirements.txt
```

- `quiz_app.py` contains the primary Gradio application.
- `quiz_data.py` contains the imported quiz-question module.
- `python_foundations_quiz.ipynb` explains the lesson concepts and includes experiments.
- `README.md` documents the project.
- `requirements.txt` lists the Gradio third-party dependency.

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

Install the third-party dependency and run the primary application:

```bash
pip install -r requirements.txt
python quiz_app.py
```

Open the local Gradio address shown in the terminal. The app does not automatically request a temporary public share URL.

## 🌐 Notebook / Google Colab Companion

The notebook presents the concepts step by step and includes small runnable experiments. It is supplementary; `quiz_app.py` remains the main local application.

Open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/python-foundations-quiz/python_foundations_quiz.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Run the setup and notebook cells in Colab. The Gradio launch cell may provide a temporary `gradio.live` share URL; open that link in a browser to test the quiz online. The link is temporary and is not a permanent deployment. `quiz_app.py` remains the primary application, while the notebook is a learning and testing companion. This project does not claim a permanent Hugging Face Spaces deployment.

## 💡 Example Interaction

```text
Question: Which keyword is used to define a function?
Answer: def
Feedback: Correct! 🎉
```

For an incorrect answer, the app gives a short explanation, such as: `Not quite. The def keyword starts a function definition in Python.`

## 📚 What I Learned

This project practices separating data into a local module, importing a constant, working with lists of dictionaries, and using list comprehensions and `enumerate()` for practical tasks. It also connects a virtual-environment workflow and `requirements.txt` with Gradio components and event handlers.

## 📝 Notes

- The questions are intentionally simple so the application can focus on demonstrating Gradio and beginner Python concepts.
- Gradio is a third-party dependency; Python standard-library modules are not listed in `requirements.txt`.
- The notebook is a learning/testing companion and is not required to run the local script.
- Hugging Face Spaces could be a possible future deployment path, but this project does not claim a completed deployment.
- The local Gradio application has been manually tested in a browser.
- No score tracking, account system, database, API, custom JavaScript, or custom CSS is included.
