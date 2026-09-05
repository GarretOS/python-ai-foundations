# 🔐 Secure Password Generator

Secure Password Generator is the first Intermediate Python portfolio project in this repository. It generates random passwords based on user-selected criteria, including password length, numbers, special characters, and uppercase letters. It also provides a simple project-defined strength assessment.

## 🎯 Project Overview

The program asks the user for a password length of at least 8 characters and whether to include each optional character group. It builds a character pool from those choices, generates a password, and reports whether the result is `Weak`, `Medium`, or `Strong` according to the project's educational scoring rule.

## ✨ Features

- User-selected password length
- Minimum length validation
- Optional numbers
- Optional special characters
- Optional uppercase letters
- Validated yes/no choices accepting `yes` / `y` and `no` / `n`
- Random password generation
- Simple `Weak` / `Medium` / `Strong` assessment
- Error handling for invalid length input
- Mini unit test for generated password length

## 🐍 Python Concepts

- The built-in `random` module
- Functions, parameters, arguments, and return values
- `for` loops and `range()`
- `_` as the conventional loop variable when the loop value is intentionally unused
- Booleans
- Input validation with `while True` and `return True` / `return False`
- Integer conversion with `int()`
- `try` / `except ValueError`
- `continue` and `break`
- String concatenation
- `len()`
- Mini unit testing
- `if __name__ == "__main__":`

## 🧩 How It Works

The `generate_password()` function starts with lowercase letters and adds numbers, special characters, or uppercase letters when the user selects them. It then loops `length` times, uses `random.choice()` to select one character from the available pool, and concatenates each selection into the password string. The completed password is returned to the caller.

The `check_password_strength()` function starts with the password length and adds project-defined points for the selected character groups. Scores below 10 are `Weak`, scores below 16 are `Medium`, and all other scores are `Strong`.

## 📁 Project Structure

```text
secure-password-generator/
├── README.md
├── secure_password_generator.py
├── secure_password_generator.ipynb
└── requirements.txt
```

- `secure_password_generator.py` contains the local Python script.
- `secure_password_generator.ipynb` presents the project for Jupyter or Google Colab.
- `README.md` documents the project.
- `requirements.txt` documents that no third-party dependencies are required.

## 🚀 How to Run

### Run the Python script

Python 3 is required. From this project directory, run:

```bash
python secure_password_generator.py
```

You can also use:

```bash
python3 secure_password_generator.py
```

Enter a password length of at least 8, then answer `yes` / `y` or `no` / `n` for each optional character group. Invalid responses are rejected and the same question is asked again.

### Run in Google Colab

Open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/secure-password-generator/secure_password_generator.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 💡 Example Output

```text
Enter password length (minimum 8): 12
Include numbers? (yes/no): yes
Include special characters? (yes/no): yes
Include uppercase letters? (yes/no): y
Generated password: aB7!mQ2x#kLp
Password strength: Strong
```

The generated password is random, so a different password will normally appear on each run.

## 📚 What I Learned

This project practices organizing a program with functions, passing arguments to parameters, returning values, building strings with concatenation, and repeating work with `for` loops and `range()`. It also applies input conversion, `ValueError` handling, loop control with `continue` and `break`, Boolean choices, a simple strength calculation, and the `test_generate_password()` mini unit test.

## 📝 Notes

- Random output changes on each run.
- Enabling a character group adds it to the available pool but does not guarantee that at least one character from that group appears.
- The `Weak` / `Medium` / `Strong` score is a simple educational project rule, not a professional cybersecurity measurement.
- No third-party packages are required.
