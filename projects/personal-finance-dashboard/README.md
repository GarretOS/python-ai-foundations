# 💰 Personal Finance Dashboard

Personal Finance Dashboard is the fourth and final Intermediate Python portfolio project in this repository. It stores financial transactions in a CSV file, reads them with pandas, displays a financial summary, and creates interactive Plotly charts.

## 🎯 Project Overview

The program accepts income and expense transactions until the user types `done`. Each valid transaction is appended to `finance_data.csv`. The program then calculates total income, total expenses, and net balance before displaying three interactive views of the data.

## ✨ Features

- Multiple transaction entry
- Persistent CSV file storage
- Date, amount, category, and transaction-type validation
- Positive US dollar amounts for both income and expenses
- Pandas DataFrame reading and summaries
- Income vs. Expenses bar chart
- Expenses by Category pie chart
- Daily Income and Expense Trend line chart
- Clear handling for missing data and expense-free data

## 🐍 Python Concepts

- CSV file storage with `open()`, `with open(...)`, append mode, and `file.write()`
- `os.path.exists()` and `os.stat()`
- pandas and `pd.read_csv()`
- DataFrames and DataFrame column selection
- `groupby()`, `sum()`, and `reset_index()`
- `pd.to_datetime()` and `datetime.strptime()`
- Plotly Express with `px.bar()`, `px.pie()`, and `px.line()`
- Figure objects and `.show()`
- Functions, loops, input validation, and `if __name__ == "__main__":`

## 🧩 How It Works

`input_transaction()` repeatedly validates a date, positive amount, category, and transaction type. `write_transaction_to_file()` opens the file in append mode and writes the header only when the file is new or empty. `read_transactions_from_file()` returns a pandas DataFrame, including an empty DataFrame with consistent columns when no file exists.

The summary separates `income` and `expense` rows and calculates `Net Balance` as total income minus total expenses. `show_charts()` groups the data for the three Plotly Express charts and converts dates with the explicit `%Y-%m-%d` format.

## 📁 Project Structure

```text
personal-finance-dashboard/
├── README.md
├── personal_finance_dashboard.py
├── personal_finance_dashboard.ipynb
└── requirements.txt
```

- `personal_finance_dashboard.py` contains the local Python script.
- `personal_finance_dashboard.ipynb` presents the project for Jupyter or Google Colab.
- `README.md` documents the project.
- `requirements.txt` lists the pandas and Plotly dependencies.

## 🚀 Running Locally

Python 3 is required. From this project directory, create and activate a virtual environment if desired, install the dependencies, and run:

```bash
pip install -r requirements.txt
python personal_finance_dashboard.py
```

Enter transactions one at a time. Type `done` at the date prompt when finished. The script then prints the summary and opens the charts in the Plotly viewer available in your environment.

## 🌐 Google Colab

Open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/personal-finance-dashboard/personal_finance_dashboard.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 💡 Example Output

```text
=== Financial Summary ===
Total Income:   $3,500.00
Total Expenses: $700.00
Net Balance:    $2,800.00
```

The bar chart compares the $3,500 income total with the $700 expense total. The pie chart shows Groceries as the largest expense category at $450. The line chart shows income peaking at $3,000 on 2026-09-01 and the largest expense day as 2026-09-02 at $350.

## 📊 Interactive Dashboard

- **Income vs. Expenses** uses `Type` and summed `Amount` values in a bar chart.
- **Expenses by Category** filters to expense rows, then groups by `Category` and sums `Amount`.
- **Daily Income and Expense Trend** converts `Date` to datetime values and sums transactions by date and type.

## 📚 What I Learned

This project practices storing data in a plain CSV file and loading it into a pandas DataFrame. It also connects validation, grouping and summarizing data, date conversion, and creating interactive Plotly figures in one practical application.

## 📝 Notes

- All amounts use US dollars and are stored as positive numbers. Expenses are not stored as negative numbers.
- `finance_data.csv` is generated at runtime and is not part of the committed project source.
- Existing transactions remain in the CSV between runs. For a fresh experiment, remove the runtime CSV before entering data again.
- The project uses pandas and Plotly; `os` and `datetime` are Python standard-library modules and are not listed in `requirements.txt`.
