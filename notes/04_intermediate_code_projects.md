# Section 4: Intermediate Code Projects

**Course:** Python for AI Engineering (Towards AI Academy)
**Instructor:** Louis-François Bouchard
**Status:** Complete

---

## What This Section Covers

Section 4 moves from the small standalone programs in the Beginner Code Projects section into four more realistic portfolio applications: a Secure Password Generator, a Python Learning Resource Scraper, a Python Foundations Quiz, and a Personal Finance Dashboard.

The projects build on the earlier fundamentals while introducing reusable functions, multiple Python files, third-party packages, network requests, concurrent work, a web interface, persistent storage, structured data analysis, interactive charts, and project-level dependency management. The emphasis is not only on writing code that runs, but on validating inputs, handling expected failures, testing real behavior, and organizing a project so it can be run again in a controlled environment.

---

## From Beginner Scripts to Reusable Programs

### Modules, Imports, and Dependencies

A module is a Python file that can be imported by another file. Python also includes a standard library: modules such as `random`, `threading`, `os`, and `datetime` are available without being installed separately. Third-party packages such as `requests`, `beautifulsoup4`, `gradio`, `pandas`, and `plotly` are installed with `pip` and recorded in `requirements.txt`.

The four projects make this distinction concrete:

- The password generator uses only the standard library, so its requirements file has no third-party dependencies.
- The scraper adds `requests` for HTTP requests and BeautifulSoup for HTML parsing. Its `threading` import is still part of the standard library.
- The quiz uses Gradio to build a browser-based interface.
- The finance dashboard uses pandas for data analysis and Plotly for visualization.

A virtual environment keeps a project's installed packages isolated from other projects. A typical workflow is:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

`pip` installs the packages listed by the project, while `requirements.txt` documents what another environment needs in order to run it. Dependency management becomes more important as a project combines more external libraries.

### Functions, Parameters, Arguments, and Return Values

The projects use functions to give each piece of behavior a clear responsibility. A parameter is the name in a function definition; an argument is the value passed by the caller. A return value sends a result back to the caller.

```python
def generate_password(length, include_numbers, include_special, include_uppercase):
    # build and return a password
    return password
```

Functions also call other functions. The password generator's `main()` collects input, `get_yes_no()` handles repeated Boolean choices, `generate_password()` creates the result, and `check_password_strength()` evaluates it. The finance dashboard similarly separates input, file writing, file reading, summary calculation, and chart creation.

The `if __name__ == "__main__":` guard controls whether a file runs its application entry point when executed directly. It prevents the interactive application from launching automatically when functions or data are imported from another file.

---

## Secure Password Generator

The password generator extends basic loops and conditionals into a small collection of reusable functions. It builds a character string from lowercase letters and optional numbers, special characters, and uppercase letters. `random.choice(characters)` selects one character from that pool each time through the loop:

```python
for _ in range(length):
    password += random.choice(characters)
```

`range(length)` produces the requested number of loop iterations. The conventional `_` loop variable communicates that the iteration value itself is intentionally unused; only the repetition matters. The completed string is returned to the caller.

The project also practices input validation. The password length is converted with `int()`, rejected when it is below 8, and protected by `try`/`except ValueError` when the user enters something that is not a whole number. `get_yes_no()` uses `while True` until the input is an accepted form of yes or no, then returns `True` or `False`. `continue` retries invalid length input, while `break` exits after a valid password has been generated.

`test_generate_password()` is a small manual unit test: it generates a 12-character password and checks that `len()` returns 12. This is not a complete security test, but it demonstrates testing a function's observable result rather than only checking whether the file has valid syntax. The strength label is a simple project-defined score based on length and selected character groups, not a professional cybersecurity assessment.

---

## Web Scraping and Concurrent Requests

### HTTP GET Requests and HTML Parsing

The Python Learning Resource Scraper uses `requests.get()` to send HTTP GET requests to three official Python documentation pages. The returned `Response` object provides the page text and the HTTP status code. A ten-second timeout prevents a request from waiting indefinitely, and `requests.RequestException` is handled so a network failure becomes a result with a failed status instead of crashing the whole summary.

BeautifulSoup turns the response HTML into a searchable object:

```python
soup = BeautifulSoup(response.text, "html.parser")
```

The scraper extracts the page title from `soup.title` and the first `<h1>` element with `soup.find("h1")`. It removes documentation-specific span and permalink elements before reading the heading text. Missing titles or headings receive fallback text. This is the core pattern of HTML parsing: fetch a document, construct a parser object, locate elements, clean the extracted content, and return structured data.

The scraper also demonstrates several Python language features. `scrape_resource(url, verbose=False)` has a default function argument, so callers can omit `verbose` when normal output is wanted. A nested `show_info()` function can access `local_info` from its enclosing function and `GLOBAL_VERSION` from the module scope. This is a practical example of LEGB scope: Python looks for names in Local, Enclosing, Global, and Built-in scopes. The title extraction uses a small `lambda` function for a one-expression transformation.

### Threading and Preserving Result Order

The three pages are independent network tasks, so the project uses `threading.Thread` to overlap the waiting time for their requests. Each thread receives a `target` function and `args` tuple:

```python
thread = threading.Thread(
    target=update_results,
    args=(i, link, results, True),
)
```

Calling `start()` begins a thread. Calling `join()` makes the main program wait for that thread to finish. The scraper starts every worker before joining them, then prints the results only after all requests are complete.

Concurrency means completion order can differ from input order. The project preserves stable display order by giving each URL its original index and having each worker write to that position in the shared `results` list. The requests can finish in any order, but the final list still matches the order of the source URLs.

---

## Multi-File Python and a Gradio Web Interface

The Python Foundations Quiz separates its data from its application. `quiz_data.py` defines the `QUIZ_QUESTIONS` list, and `quiz_app.py` imports it. This is a small but important step beyond a single-file script: project files can have distinct responsibilities and can import values from one another.

The application uses a list comprehension to extract the question text:

```python
return [question["question"] for question in QUIZ_QUESTIONS]
```

`enumerate()` supplies both an index and an item while searching for the selected question. If no question matches, `find_question_index()` returns `None`. `None` represents the absence of a result, which lets the interface distinguish “not found” from a valid index such as `0`.

Gradio provides the browser-facing components: a `Dropdown` selects a question, a `Textbox` displays it, a `Radio` shows the answer choices, and a `Button` checks the answer. The components are created inside `with gr.Blocks() as demo:`, which groups the interface definition. Gradio components are objects with properties and methods, so this project gives a first practical encounter with classes and objects through a library rather than through a custom class definition.

The interface is event-driven. The dropdown's `.change()` event calls `quiz_interface`, and the button's `.click()` event calls `check_answer`. The functions are passed without calling them:

```python
check_button.click(
    fn=check_answer,
    inputs=[question_selector, answer_options],
    outputs=feedback_display,
)
```

`fn=check_answer` passes the function object so Gradio can call it later when the event occurs. Writing `fn=check_answer()` would call it immediately while the interface is being built, which is not the desired event-driven behavior.

The local script and the notebook have different execution contexts. The script can import its sibling `quiz_data.py` normally. A notebook opened by itself in Google Colab does not automatically copy sibling files into the runtime, so the notebook includes a self-contained dataset for its demonstrations. Installing Gradio with `pip`, running `demo.launch()`, and testing the temporary browser URL in Colab verifies actual interface behavior rather than only checking that the Python parses.

---

## Persistent Data, pandas, and Interactive Visualization

### CSV Storage and Validation

The Personal Finance Dashboard introduces persistent data: transactions remain in `finance_data.csv` between runs. `open()` with `"a"` append mode adds new rows without replacing existing rows. The `with` statement manages the file context and closes the file after writing. The header is written only when the file is new or empty, and `file.write()` stores each validated transaction as a CSV row.

`input_transaction()` validates each field before returning it. `datetime.strptime()` checks that the date follows `YYYY-MM-DD`; `float()` converts the amount and `ValueError` handles non-numeric input; amounts must be greater than zero; categories cannot be empty; and the type must be `income` or `expense`. Typing `done` at the date prompt returns `None`, which signals the main loop to stop collecting transactions. This uses `None` as a deliberate control value, not as an error.

### DataFrames, Series, and Aggregation

`pd.read_csv()` loads the stored rows into a pandas DataFrame. A DataFrame is a table-like object with rows and named columns; selecting one column produces a pandas Series. The dashboard filters rows with Boolean conditions, such as selecting only expense transactions, and uses `sum()` to calculate totals.

Grouped summaries prepare data for both the printed summary and the charts:

```python
category_totals = (
    expenses.groupby("Category")["Amount"].sum().reset_index()
)
```

`groupby()` partitions rows by a key, `sum()` aggregates the amount in each group, and `reset_index()` turns the grouping result back into ordinary columns suitable for charting. Income and expense amounts are stored as positive values; the `Type` column determines whether a row contributes to income or expenses, and net balance is total income minus total expenses.

CSV dates begin as text. `pd.to_datetime()` converts the `Date` column to datetime values so pandas can sort and group dates correctly. The dashboard uses the explicit `%Y-%m-%d` format and drops invalid converted dates before building the trend data.

### Plotly Express and Figure Objects

Plotly Express creates interactive Figure objects from prepared tabular data:

- `px.bar()` compares total income and expenses.
- `px.pie()` shows expense totals grouped by category.
- `px.line()` shows daily income and expense trends, with markers and a separate color for each type.

The visualization step depends on preparing the data first: filter the relevant rows, group and sum the values, convert dates, sort the daily results, and then pass the resulting DataFrame to Plotly. An expense-free dataset skips the category pie chart, while an empty or missing file is represented by a DataFrame with the expected columns and produces a zero-valued summary.

---

## Testing Real Runtime Behavior

Across the four projects, correctness means more than passing a syntax check. The password generator checks a generated length. The scraper needs real HTTP requests, timeout behavior, HTML extraction, and stable ordering. The quiz needs its Gradio callbacks to update components correctly in a browser. The finance dashboard needs file persistence, validation loops, DataFrame calculations, and charts to work with both normal and missing or limited data.

The notebooks provide an additional learning and testing surface. They explain the code in Markdown, run focused examples, and in several cases use controlled data so the analysis can be repeated without changing runtime files. Google Colab and browser checks exposed practical environment concerns such as installing third-party packages, handling sibling modules, and opening temporary Gradio share links. These are part of validating a project as a user would experience it, not just as source text.

The main lesson is to test the path a user will actually take: invalid inputs, missing data, network failures, empty results, repeated runs, and successful end-to-end interaction all matter.

---

## Key Takeaways

1. Functions make programs reusable and easier to reason about; parameters receive arguments, and return values connect one function to another.
2. Standard-library modules and third-party packages have different installation and documentation responsibilities.
3. `try`/`except ValueError` and deliberate validation loops turn common bad input into recoverable program behavior.
4. `random.choice()` and `range()` support repeated random selection, while `_` communicates an intentionally unused loop value.
5. `__name__ == "__main__"` separates direct script execution from importing a module.
6. HTTP requests, `Response` objects, timeouts, exceptions, and HTML parsing are the basic pieces of a practical scraper.
7. Threads can overlap independent network work; indexed result storage preserves the original order even when completion order changes.
8. Multiple files and imports let data and application logic have separate responsibilities.
9. Gradio introduces components, objects, and event-driven callbacks; callback functions are passed to events without being called immediately.
10. CSV files provide simple persistent storage, while pandas provides DataFrames, Series, filtering, grouping, aggregation, and date-aware analysis.
11. Plotly charts are built from appropriately prepared data, and Figure objects make the results interactive.
12. Dependency files, virtual environments, notebooks, Colab, and browser testing are part of building reproducible Python projects.
13. The progression from beginner scripts to these projects adds reusable functions, modules, packages, networking, concurrency, interfaces, persistence, analysis, and visualization.

---

## Projects

- [Secure Password Generator](../projects/secure-password-generator/)
- [Python Learning Resource Scraper](../projects/python-learning-resource-scraper/)
- [Python Foundations Quiz](../projects/python-foundations-quiz/)
- [Personal Finance Dashboard](../projects/personal-finance-dashboard/)

---

## Resources

- Project READMEs and notebooks in the four project directories above
- Google Colab notebooks linked from each project README
