# 🍔 Food Truck Sales Analyzer

Food Truck Sales Analyzer is a beginner Python project that studies one week of fictional sales data from the Stack Attack burger truck.

## 🎯 Project Overview

The program calculates average daily revenue, total weekly revenue, the busiest burger-sales day, weekday and weekend burger averages, and the number of days that met a burger-sales target. It also compares burger and drink sales and looks at the relationship between above-average burger sales and revenue.

## ✨ Features

- Weekly sales data stored in a dictionary
- Average daily revenue
- Total weekly revenue
- Busiest burger-sales day
- Above-average burger and revenue comparison
- Weekday versus weekend burger averages
- Burger sales target count
- Total burger and drink comparison
- Final weekly summary

## 🐍 Python Concepts

- Dictionaries and lists
- Variables and strings
- Integers and floats
- `for` loops and `while` loops
- `if`, `elif`, and `else`
- Comparisons and arithmetic
- `len()` for counting items
- f-strings for formatted output
- Comments

## 📊 Analysis Concepts

- Average daily revenue is total revenue divided by the number of days.
- The busiest day is found by comparing burger counts with a running maximum.
- The simple relationship check counts above-average burger days and then checks their revenue. This is not statistical correlation.
- Weekday and weekend averages are calculated with separate totals and counters.
- The burger target uses `>=`, so a day exactly at the target would count.
- Comparing totals is a small extension using concepts already learned.

## 📁 Project Structure

```text
food-truck-sales-analyzer/
├── README.md
├── food_truck_sales.py
├── food_truck_sales_analyzer.ipynb
└── requirements.txt
```

- `food_truck_sales.py` contains the complete Python script.
- `food_truck_sales_analyzer.ipynb` contains the notebook version for Jupyter or Google Colab.
- `requirements.txt` documents that no third-party dependencies are required.

## 🚀 How to Run

Python 3 is required. From this project directory, run:

```bash
python food_truck_sales.py
```

You can also open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/food-truck-sales-analyzer/food_truck_sales_analyzer.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 💡 Example Output

```text
=== Stack Attack Weekly Sales Analysis ===
Average daily revenue: $767.86
Busiest burger-sales day: Saturday with 96 burgers sold
Total weekly revenue: $5,375.00
Above-average burger days also having above-average revenue: 2 out of 3
Simple relationship ratio: 0.67
Average weekday burger sales: 56.6
Average weekend burger sales: 89.5
Days meeting the 70-burger target: 3
Total burgers sold: 462
Total drinks sold: 340
Higher-selling category: burgers

=== Final Summary ===
Weekly revenue: $5,375.00
Average daily revenue: $767.86
Busiest day: Saturday (96 burgers)
Weekday vs. weekend averages: 56.6 vs. 89.5
Days meeting target: 3
```

## 📚 What I Learned

This project practices organizing related weekly data in a dictionary, processing lists with loops, using conditions to compare values, and presenting calculated results with formatted strings. It intentionally uses only Python's built-in features.

## 📝 Notes

The Stack Attack sales data is fictional. The relationship check is a simple comparison of counts, not statistical correlation. The burgers-versus-drinks comparison is a small extension using concepts already learned. The project intentionally stays within the introductory lesson scope and does not use third-party libraries.
