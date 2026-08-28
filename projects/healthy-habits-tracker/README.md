# Healthy Habits Tracker

Healthy Habits Tracker is a beginner Python project for recording daily water, exercise, and sleep entries. Each habit can have multiple entries, and the entries accumulate toward that habit's daily goal.

## Project Overview

The program lets you choose a supported habit, enter an amount, and see the accumulated total for that habit. It reports whether the daily goal has been reached and displays a summary of all habits when you type `done`.

## Features

- Track water toward an 8-cup daily goal
- Track exercise toward a 30-minute daily goal
- Track sleep toward a 7-hour daily goal
- Record multiple entries for each habit
- Accumulate entries toward each habit's daily goal
- Reject negative values
- Reject sleep entries greater than 24 hours
- Handle invalid numeric input
- Display a final summary and count completed goals

## Python Concepts Used

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

The project intentionally stays within the Python concepts introduced in the lesson. It does not use functions, classes, external libraries, file storage, dates, or APIs.

## How to Run Locally

Python 3 is required. From the project directory, run:

```bash
python healthy_habits_tracker.py
```

Choose `water`, `exercise`, or `sleep`, enter an amount, and continue recording entries. Type `done` when you are finished.

## Interactive Google Colab Notebook

Open the notebook in Google Colab using the badge at the top of `healthy_habits_tracker.ipynb`. Run the implementation cell and interact with the tracker directly in Colab when prompted.

## Project Structure

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
