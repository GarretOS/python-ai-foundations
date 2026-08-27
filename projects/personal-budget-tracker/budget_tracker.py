# Personal Budget Tracker

# A simple daily tool for tracking income, expenses, and savings.

print("\n=== Personal Budget Tracker ===")
print("Track your money for today and keep an eye on your savings goal.\n")

# Collect today's financial information.

daily_income = float(input("Enter today's income: "))
daily_expenses = float(input("Enter today's expenses (excluding rent): "))
rent_expense = float(input("Enter today's rent expense: "))

# Combine expenses and calculate the amount left after spending.

total_expenses = daily_expenses + rent_expense
net_savings = daily_income - total_expenses

# Collect a future savings target and an optional note.

savings_goal = float(input("Enter your future savings goal: "))
daily_note = input("Add a note about today (optional): ")

# Display the day's financial summary.

print("\n=== Daily Summary ===")
print("Income:       $", daily_income)
print("Expenses:     $", total_expenses)
print("Net savings:  $", net_savings)
print("Savings goal: $", savings_goal)
print("Note:         ", daily_note)

# Provide a concise summary of the day's finances.

print(
    f"\nToday you earned ${daily_income:.2f}, "
    f"spent ${total_expenses:.2f}, "
    f"and saved ${net_savings:.2f}."
)
