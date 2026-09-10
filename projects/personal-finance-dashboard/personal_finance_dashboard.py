import os
from datetime import datetime

import pandas as pd
import plotly.express as px


CSV_FILENAME = "finance_data.csv"


def write_transaction_to_file(date, amount, category, transaction_type):
    """Append one transaction to the CSV file, adding a header when needed."""
    file_is_new = not os.path.exists(CSV_FILENAME)
    file_is_empty = not file_is_new and os.stat(CSV_FILENAME).st_size == 0

    with open(CSV_FILENAME, "a", encoding="utf-8") as file:
        if file_is_new or file_is_empty:
            file.write("Date,Amount,Category,Type\n")

        file.write(f"{date},{amount},{category},{transaction_type}\n")


def read_transactions_from_file():
    columns = ["Date", "Amount", "Category", "Type"]

    if not os.path.exists(CSV_FILENAME):
        return pd.DataFrame(columns=columns)

    return pd.read_csv(CSV_FILENAME)


def input_transaction():
    while True:
        date_text = input("Date (YYYY-MM-DD, or done to finish): ").strip()

        if date_text.lower() == "done":
            return None

        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")

    while True:
        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break
        except ValueError:
            print("Please enter a valid number for the amount.")

    while True:
        category = input("Category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    while True:
        transaction_type = input("Type (income/expense): ").strip().lower()

        if transaction_type == "income" or transaction_type == "expense":
            break

        print("Please enter income or expense.")

    return date_text, amount, category, transaction_type


def show_summary(df):
    if df.empty:
        total_income = 0
        total_expenses = 0
    else:
        total_income = df.loc[df["Type"] == "income", "Amount"].sum()
        total_expenses = df.loc[df["Type"] == "expense", "Amount"].sum()

    net_balance = total_income - total_expenses

    print("\n=== Financial Summary ===")
    print(f"Total Income:   ${total_income:,.2f}")
    print(f"Total Expenses: ${total_expenses:,.2f}")
    print(f"Net Balance:    ${net_balance:,.2f}")


def show_charts(df):
    totals = df.groupby("Type")["Amount"].sum().reset_index()
    income_expense_chart = px.bar(
        totals,
        x="Type",
        y="Amount",
        title="Income vs. Expenses",
    )
    income_expense_chart.show()

    expenses = df[df["Type"] == "expense"]
    if expenses.empty:
        print("No expenses exist, so the Expenses by Category chart was skipped.")
    else:
        category_totals = (
            expenses.groupby("Category")["Amount"].sum().reset_index()
        )
        expenses_by_category_chart = px.pie(
            category_totals,
            names="Category",
            values="Amount",
            title="Expenses by Category",
        )
        expenses_by_category_chart.show()

    chart_data = df.copy()
    chart_data["Date"] = pd.to_datetime(
        chart_data["Date"], format="%Y-%m-%d", errors="coerce"
    )
    chart_data = chart_data.dropna(subset=["Date"])
    daily_totals = (
        chart_data.groupby(["Date", "Type"])["Amount"].sum().reset_index()
    )
    daily_totals = daily_totals.sort_values("Date")
    daily_trend_chart = px.line(
        daily_totals,
        x="Date",
        y="Amount",
        color="Type",
        title="Daily Income and Expense Trend",
    )
    daily_trend_chart.show()


def main():
    print("=== Personal Finance Dashboard ===")
    print("Enter transactions, or type done at the date prompt to finish.")

    while True:
        transaction = input_transaction()

        if transaction is None:
            break

        write_transaction_to_file(*transaction)
        print("Transaction saved.")

    transactions = read_transactions_from_file()
    show_summary(transactions)
    show_charts(transactions)


if __name__ == "__main__":
    main()
