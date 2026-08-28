# 🏃 Healthy Habits Tracker

Healthy Habits Tracker is a beginner Python project for recording daily water, exercise, and sleep entries. Each habit can have multiple entries, and the entries accumulate toward that habit's daily goal.

## 🎯 Project Overview

The program lets you choose a supported habit, enter an amount, and see the accumulated total for that habit. It reports whether the daily goal has been reached and displays a summary of all habits when you type `done`.

## ✨ Features

- Track water toward an 8-cup daily goal
- Track exercise toward a 30-minute daily goal
- Track sleep toward a 7-hour daily goal
- Record multiple entries for each habit
- Accumulate entries toward each habit's daily goal
- Reject negative values
- Reject sleep entries greater than 24 hours
- Handle invalid numeric input
- Display a final summary and count completed goals

## 🐍 Python Concepts

- Variables and constants
- Dictionaries
- Lists
- Tuples
- Strings and f-strings
- User input with `input()`
- Type conversion with `float()`
- `while` and `for` loops
- `if`, `elif`, and `else` conditionals
- `try`/`except` for invalid numeric input
- `sum()` and `len()`
- Comments and formatted output with `print()`

This project intentionally keeps the implementation simple because it is based on an introductory Python lesson.

## 📁 Project Structure

```text
healthy-habits-tracker/
├── healthy_habits_tracker.py
├── healthy_habits_tracker.ipynb
├── README.md
└── requirements.txt
```

- `healthy_habits_tracker.py` contains the local Python script.
- `healthy_habits_tracker.ipynb` presents the project and runs the same implementation in Jupyter or Google Colab.
- `README.md` documents the project.
- `requirements.txt` notes that no third-party dependencies are required.

## 🚀 How to Run

### Run the Python script

Python 3 is required. From this project directory, run:

```bash
python healthy_habits_tracker.py
```

Choose `water`, `exercise`, or `sleep`, enter an amount, and continue recording entries. Type `done` when you are finished.

### Run in Google Colab

Open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/healthy-habits-tracker/healthy_habits_tracker.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 💡 Example

```text
=== Today's Summary ===
Water: 8 / 8
Status: Goal reached!
Entries recorded: 2

Exercise: 30 / 30
Status: Goal reached!
Entries recorded: 1

Sleep: 6.5 / 7
Status: Goal not reached yet.
Entries recorded: 1

You completed 2 out of 3 daily goals.
Thanks for using the Healthy Habits Tracker!
```

## 📚 What I Learned

This project practices storing related values in dictionaries and lists, collecting user input, converting text input into numbers with `float()`, repeating interactions with `while` and `for` loops, and validating input with conditionals and `try`/`except`. It also uses `sum()` and `len()` to calculate totals and count entries.

## 📝 Notes

This project intentionally does not use functions, classes, external libraries, dates, APIs, databases, or file storage because those concepts are outside the scope of this introductory lesson.
