# Food Truck Sales Analyzer

# Weekly sales data for the fictional Stack Attack burger truck
food_truck_sales = {
    "day": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ],
    "burgers_sold": [46, 53, 49, 61, 74, 96, 83],
    "drinks_sold": [31, 40, 34, 55, 47, 71, 62],
    "revenue": [520, 610, 565, 850, 760, 1115, 955]
}

print("\n=== Stack Attack Weekly Sales Analysis ===")

# Calculate average daily revenue
revenue_list = food_truck_sales["revenue"]

total_revenue = 0

for amount in revenue_list:
    total_revenue = total_revenue + amount

average_revenue = total_revenue / len(revenue_list)

print(f"Average daily revenue: ${average_revenue:.2f}")

# Find the day with the highest burger sales
burger_list = food_truck_sales["burgers_sold"]
day_list = food_truck_sales["day"]

max_burgers = 0
max_day = ""

index = 0

while index < len(burger_list):
    if burger_list[index] > max_burgers:
        max_burgers = burger_list[index]
        max_day = day_list[index]

    index = index + 1

print(
    f"Busiest burger-sales day: "
    f"{max_day} with {max_burgers} burgers sold"
)

# Calculate total weekly revenue
weekly_revenue = 0

for amount in revenue_list:
    weekly_revenue = weekly_revenue + amount

print(f"Total weekly revenue: ${weekly_revenue:,.2f}")

# Compare above-average burger sales with above-average revenue
total_burgers = 0

for burgers in burger_list:
    total_burgers = total_burgers + burgers

average_burgers = total_burgers / len(burger_list)

days_burgers_above_average = 0
days_burgers_and_revenue_above_average = 0

index = 0

while index < len(burger_list):
    if burger_list[index] > average_burgers:
        days_burgers_above_average = days_burgers_above_average + 1

        if revenue_list[index] > average_revenue:
            days_burgers_and_revenue_above_average = (
                days_burgers_and_revenue_above_average + 1
            )

    index = index + 1

if days_burgers_above_average > 0:
    relationship_ratio = (
        days_burgers_and_revenue_above_average
        / days_burgers_above_average
    )
else:
    relationship_ratio = 0

print(
    "Above-average burger days also having above-average revenue: "
    f"{days_burgers_and_revenue_above_average} "
    f"out of {days_burgers_above_average}"
)

print(f"Simple relationship ratio: {relationship_ratio:.2f}")

# Compare average weekday and weekend burger sales
weekday_total = 0
weekday_count = 0
weekend_total = 0
weekend_count = 0

index = 0

while index < len(day_list):
    current_day = day_list[index]
    current_burger_sales = burger_list[index]

    if current_day == "Saturday" or current_day == "Sunday":
        weekend_total = weekend_total + current_burger_sales
        weekend_count = weekend_count + 1
    else:
        weekday_total = weekday_total + current_burger_sales
        weekday_count = weekday_count + 1

    index = index + 1

if weekday_count != 0:
    average_weekday_burgers = weekday_total / weekday_count
else:
    average_weekday_burgers = 0

if weekend_count != 0:
    average_weekend_burgers = weekend_total / weekend_count
else:
    average_weekend_burgers = 0

print(
    f"Average weekday burger sales: "
    f"{average_weekday_burgers:.1f}"
)

print(
    f"Average weekend burger sales: "
    f"{average_weekend_burgers:.1f}"
)

# Count the days that met the burger sales target
threshold = 70
days_meeting_target = 0

for burgers in burger_list:
    if burgers >= threshold:
        days_meeting_target = days_meeting_target + 1

print(
    f"Days meeting the {threshold}-burger target: "
    f"{days_meeting_target}"
)

# Compare total burgers and drinks sold
drink_list = food_truck_sales["drinks_sold"]

total_drinks = 0

for drinks in drink_list:
    total_drinks = total_drinks + drinks

print(f"Total burgers sold: {total_burgers}")
print(f"Total drinks sold: {total_drinks}")

if total_burgers > total_drinks:
    higher_selling_category = "burgers"
elif total_drinks > total_burgers:
    higher_selling_category = "drinks"
else:
    higher_selling_category = "both categories equally"

print(f"Higher-selling category: {higher_selling_category}")

# Display a concise weekly summary
print("\n=== Final Summary ===")
print(f"Weekly revenue: ${weekly_revenue:,.2f}")
print(f"Average daily revenue: ${average_revenue:.2f}")
print(f"Busiest day: {max_day} ({max_burgers} burgers)")

print(
    f"Weekday vs. weekend averages: "
    f"{average_weekday_burgers:.1f} vs. "
    f"{average_weekend_burgers:.1f}"
)

print(f"Days meeting target: {days_meeting_target}")
