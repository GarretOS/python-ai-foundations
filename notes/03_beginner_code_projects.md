# Section 3: Beginner Code Projects

**Course:** Python for AI Engineering (Towards AI Academy)
**Instructor:** Louis-François Bouchard
**Status:** Complete

---

## What This Section Covers

Section 3 turns the fundamentals into four small applications: a Personal Budget Tracker, a Healthy Habits Tracker, a Food Truck Sales Analyzer, and a Lost Temple Adventure. The projects are different on the surface, but the same building blocks appear repeatedly: store values in variables and data structures, collect or process input, use control flow to make decisions, and display or validate results.

The projects also introduced the practical difference between running a Python script and working interactively in a notebook, along with the tools needed to manage Python projects.

---

## Building a Small Python Program

### Scripts, Variables, and Output

A Python script is a text file containing Python statements, usually saved with a `.py` extension. It can be run from a terminal:

```bash
python budget_tracker.py
```

The program executes its statements in order. Variables give useful names to values so the program can use them later:

```python
daily_income = 187.50
rent_expense = 45.00
net_savings = daily_income - rent_expense
```

The main types used in these projects were:

- `str`: text, such as `"Saturday"`
- `int`: whole numbers, such as `70`
- `float`: numbers with decimal values, such as `767.86`

`input()` reads text typed by the user, even when the user types a number. `float()` converts numeric text into a floating-point value so arithmetic can be performed. `print()` displays a result.

```python
amount = float(input("Enter an amount: "))
print(f"Amount recorded: ${amount:.2f}")
```

Comments begin with `#`. They are ignored by Python but explain the purpose of code to a future reader or to yourself when you return to the project.

### Arithmetic and f-Strings

The budget tracker combines expenses and subtracts them from income:

```python
total_expenses = daily_expenses + rent_expense
net_savings = daily_income - total_expenses
```

An f-string lets an expression be inserted directly into a string. A format specifier controls how a value is displayed:

```python
print(f"Weekly revenue: ${weekly_revenue:,.2f}")
```

Here, `,` adds thousands separators and `.2f` displays two digits after the decimal point. Formatting changes how a value is shown; it does not change the underlying value.

---

## Collections and Repeated Input: Healthy Habits Tracker

### Lists, Dictionaries, and Tuples

A list is an ordered, mutable collection. It is useful when values need to be added during a program:

```python
water_entries = []
water_entries.append(4)
water_entries.append(2)
```

`.append()` is a list method: it adds one item to the end of the list. The tracker stores multiple entries for each habit in a dictionary of lists:

```python
habits_data = {
    "water": [],
    "exercise": [],
    "sleep": []
}
```

A dictionary stores key/value relationships. A key such as `"water"` identifies its corresponding value, which here is a list of entries. A tuple is also ordered, but unlike a list it is immutable. The tracker uses a tuple for the supported habit names:

```python
HABIT_NAMES = ("water", "exercise", "sleep")
```

The uppercase name is a convention that signals a constant: a value the program is intended not to change. Python does not enforce this convention.

### Control Flow and Indentation

Control flow determines which statements run and how often. `if`, `elif`, and `else` select among alternatives:

```python
if current_total >= daily_goal:
    print("Goal reached!")
else:
    print("Keep going!")
```

Comparison operators produce a true or false result. Common examples are `>`, `<`, `>=`, `<=`, `==`, and `!=`. Indentation is part of Python syntax: the indented statements belong to the condition or loop above them.

The `while` loop repeats while its condition remains true. The tracker uses one to keep accepting entries until the user types `done`. A `for` loop is useful when visiting every habit in the final summary:

```python
for habit in HABIT_NAMES:
    print(habit)
```

`break` exits the nearest loop immediately. `continue` skips the rest of the current iteration and starts the next one. In the tracker, `continue` is useful after rejecting a negative amount or an unrealistic sleep value.

Membership with `in` checks whether a value belongs to a collection:

```python
if habit_choice in HABIT_NAMES:
    print("This habit is supported.")
```

### Validating Input with Exceptions

An exception is an event raised when Python cannot complete an operation normally. Converting non-numeric input with `float()` raises `ValueError`. `try`/`except` lets the program handle that expected problem and continue instead of crashing:

```python
try:
    user_value = float(input("Enter an amount: "))
except ValueError:
    print("Invalid input. Please enter a number.")
```

The `try` block contains code that might fail. The `except ValueError` block handles this particular kind of failure. This is also a basic debugging lesson: read the error type, identify the operation that raised it, and decide whether invalid user input should be rejected, corrected, or handled another way.

---

## Python Environments and Tools

### Libraries, Packages, and pip

A library is reusable code that provides functionality for other programs. A package is a distributable collection of Python code; packages can be installed with `pip`, Python's package installer. These beginner projects mainly use Python's built-in features, so their `requirements.txt` files document that no third-party dependencies are needed.

A virtual environment is an isolated Python environment for one project. It prevents packages installed for one project from interfering with another project. A typical workflow is:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### VS Code, Jupyter, and Google Colab

VS Code is an IDE (integrated development environment): an editor with features for writing, running, and debugging code. A terminal runs commands such as `python script.py` and `pip install ...`.

Jupyter Notebook and Google Colab divide a notebook into code cells and Markdown cells. Code cells run Python; Markdown cells explain the purpose, inputs, and findings. A kernel in Jupyter, or a runtime in Colab, is the active environment that executes the code. Notebook state persists between cells, so running cells out of order can produce confusing results.

Scripts are useful for repeatable programs that run from start to finish. Notebooks are useful for exploration, explanation, and rerunning individual pieces of an analysis. The Food Truck Sales Analyzer uses the same core logic in both forms.

### Git and GitHub

Git is version control: it records changes to files over time. GitHub stores repositories remotely and makes them available for backup and collaboration. The basic workflow is:

```text
edit → save → add → commit → push
```

`git add` stages selected changes, `git commit` records a checkpoint with a message, and `git push` sends local commits to GitHub. `git status` shows the current state of the working tree. Staging only intended files is an important habit because not every local change belongs in the same commit.

---

## Notebook Data Analysis: Food Truck Sales

The Food Truck Sales Analyzer works with a small fictional weekly dataset. A dictionary of lists keeps corresponding columns together:

```python
food_truck_sales = {
    "day": ["Monday", "Tuesday", "Wednesday"],
    "burgers_sold": [46, 53, 49],
    "revenue": [520, 610, 565]
}
```

### Accumulators and Counters

An accumulator starts at zero and grows as values are processed. A counter also starts at zero, but counts occurrences rather than adding amounts:

```python
total_revenue = 0
days_meeting_target = 0

for amount in revenue_list:
    total_revenue = total_revenue + amount

for burgers in burger_list:
    if burgers >= 70:
        days_meeting_target = days_meeting_target + 1
```

An average is a total divided by the number of values. `len()` returns the number of items in a list:

```python
average_revenue = total_revenue / len(revenue_list)
```

### Indexes and a Running Maximum

Indexes connect corresponding items in separate lists. At index `2`, for example, the day, burger count, and revenue all describe the same day. A `while` loop is a natural way to traverse indexes explicitly:

```python
max_burgers = 0
max_day = ""
index = 0

while index < len(burger_list):
    if burger_list[index] > max_burgers:
        max_burgers = burger_list[index]
        max_day = day_list[index]
    index = index + 1
```

The running maximum stores both the largest value and its related day. Updating only the number would lose the connection to the item that produced it.

### Comparisons and Simple Relationships

The analyzer separates Saturday and Sunday from the weekdays with a condition, then uses separate totals and counters to calculate each average. It also checks how many days have both above-average burger sales and above-average revenue.

This is a simple relationship check, not statistical correlation. It counts matching conditions in this particular dataset; it does not measure the strength, direction, or statistical significance of a relationship. The distinction matters because a ratio such as `2 / 3` is not a correlation coefficient.

Threshold comparisons require deliberate operator choices. `>` means strictly greater than the threshold, while `>=` includes values exactly equal to it. The burger target uses `>=`, so a day with exactly 70 burgers counts.

### Notebook Workflow and Validation

The notebook combines Markdown and code: Markdown explains the question and result, while code performs the calculation. Individual cells can be rerun after changing a target or input. After rerunning, validate that the output changed as expected and that the notebook still runs from a clean, sensible order.

A notebook can be valid JSON and execute correctly while its Markdown still renders incorrectly in Google Colab. Validating notebook work therefore includes checking the rendered Markdown, not only the file structure and Python output. This is a documentation bug rather than necessarily a Python bug, but it still affects whether the notebook communicates its results correctly.

---

## Text Adventure: State, Menus, and Errors

### Nested Dictionaries and Menus

The Lost Temple Adventure uses nested dictionaries to represent locations, actions, and menu text. A nested dictionary is a dictionary whose value contains another dictionary:

```python
exploration_areas = {
    "1": {
        "name": "Stone Altar",
        "actions": {"1": "Read the inscription"}
    }
}
```

The main menu opens a second menu for a location, so nested `while` loops support multiple levels of interaction. The inner loop keeps the player in a location until `0` returns to the center. This is a useful example of stateful interaction: inventory, exploration history, and the current game state affect later choices.

Dictionary methods expose different views of the data:

- `.items()` gives key/value pairs, useful for displaying menu numbers and descriptions.
- `.keys()` gives the dictionary's keys, useful for validating a choice.
- `.get(key, default)` returns a value when a key exists, or a default when it does not. It is useful for checking optional inventory items without causing a missing-key error.

### Slicing and Indexes

String slicing extracts part of a string. The adventure uses `user_input[:1]` to select the first character from inputs such as `2 library`. List slicing extracts a portion of a list without modifying the original list:

```python
recent_history = exploration_history[-3:]
```

The negative index means “count from the end,” so `-3:` selects the last three entries. Slicing creates or extracts a portion; it does not remove that portion from the original object.

### Exceptions and Logging

Invalid menu choices are represented by `KeyError` in the game. Multiple `except` blocks can handle different problems:

```python
try:
    # interactive game action
    pass
except KeyError as error:
    logging.error("Invalid menu selection: %s", error)
except Exception as error:
    logging.error("Unexpected game error: %s", error)
finally:
    logging.info("Finished this game-loop iteration")
```

Specific handlers should normally come before a broad `Exception` handler. Otherwise the broad handler may catch the error before the specific handler gets a chance to explain it. `finally` runs whether an exception occurred or not, so it is useful for work that should always happen.

Logging sends diagnostic information to a log instead of mixing it with normal user-facing output. The `logging` module provides levels such as `INFO` and `ERROR`. `logging.basicConfig()` sets up the destination, level, and format:

```python
logging.basicConfig(
    filename="game_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
```

The format placeholders add the timestamp, level name, and message. `%s` in a logging call inserts a value into the message while letting the logging system handle formatting.

### Enum and Symbolic State

The `enum` module provides the `Enum` class. An Enum defines named members that represent a fixed set of choices:

```python
from enum import Enum

class GameState(Enum):
    TRAPPED = 0
    SEAL_FOUND = 1
    ESCAPED = 2
```

`GameState.TRAPPED` is an Enum member. The numeric values are implementation details; the names explain the program's meaning. Symbolic states are clearer and safer than scattering unexplained numbers through conditions such as `if state == 2`.

Interactive programs need behavioral testing across multiple paths: invalid choices, returning from submenus, trying the exit before finding the seal, finding an item twice, viewing history, quitting, and successfully escaping. A program that starts without a syntax error is not necessarily correct for every path a user can take.

---

## Key Takeaways

1. Small programs become manageable when values, decisions, repetition, and output are handled one clear step at a time.
2. Lists store ordered changing collections, dictionaries connect keys to values, and tuples represent ordered values that should not change.
3. `input()` returns strings, so numeric input usually needs conversion such as `float()` before arithmetic.
4. `while` loops suit repeated interaction; `for` loops suit processing each item in a collection.
5. Exceptions and basic debugging let a program respond to expected bad input without crashing.
6. Scripts are repeatable programs, while notebooks combine executable cells with explanation and exploration.
7. A running maximum must preserve related information, and indexes connect corresponding lists.
8. A simple above-average comparison is not statistical correlation.
9. Specific exception handlers should precede broad handlers, and logging separates diagnostics from normal output.
10. Enum names make program states easier to understand than unexplained numeric values.
11. Notebook rendering and interactive behavior both need validation, not just syntax or file-format checks.

---

## Projects

- [Personal Budget Tracker](../projects/personal-budget-tracker/)
- [Healthy Habits Tracker](../projects/healthy-habits-tracker/)
- [Food Truck Sales Analyzer](../projects/food-truck-sales-analyzer/)
- [Lost Temple Adventure](../projects/lost-temple-adventure/)
