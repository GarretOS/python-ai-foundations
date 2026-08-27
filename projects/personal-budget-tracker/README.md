# 💰 Personal Budget Tracker

Personal Budget Tracker is a beginner Python project for tracking daily income, expenses, rent, and savings. It collects a few values from the user and prints a simple daily financial summary.

## 🎯 Project Overview

This program allows a user to enter daily income, regular expenses, and rent. It then calculates total expenses and net savings, records a future savings goal, and includes an optional daily note.

## ✨ Features

- Daily income input
- Daily expense input
- Rent expense input
- Total expense calculation
- Net savings calculation
- Savings goal
- Optional daily note
- Formatted summary output

## 🐍 Python Concepts

- Variables
- Strings
- Floats
- User input with `input()`
- Type conversion with `float()`
- Arithmetic expressions
- `print()`
- Comments
- f-strings for output formatting

This project intentionally keeps the implementation simple because it is based on an introductory Python lesson.

## 📁 Project Structure

```text
personal-budget-tracker/
├── budget_tracker.py
├── personal_budget_tracker.ipynb
├── README.md
└── requirements.txt
```

- `budget_tracker.py` contains the Python script version of the project.
- `personal_budget_tracker.ipynb` contains the polished notebook version for Jupyter or Google Colab.
- `README.md` documents the project.
- `requirements.txt` notes that no third-party dependencies are required.

## 🚀 How to Run

### Run the Python script

Python 3 is required. From this project directory, run:

```bash
python budget_tracker.py
```

### Run in Google Colab

Open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/personal-budget-tracker/personal_budget_tracker.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 💡 Example

```text
=== Daily Summary ===
Income:       $ 187.5
Expenses:     $ 71.36
Net savings:  $ 116.14
Savings goal: $ 2500.0
Note:          Coffee and groceries

Today you earned $187.50, spent $71.36, and saved $116.14.
```

## 📚 What I Learned

This project practices storing values in variables, collecting user input, converting text input into numbers with `float()`, performing arithmetic, and displaying results with `print()`. It also uses an f-string to format the final summary output cleanly.

## 📝 Notes

This project intentionally does not use external libraries, functions, loops, conditionals, classes, databases, or file storage because those concepts are outside the scope of this introductory lesson.
