# Healthy Habits Tracker

# Daily goals for each habit
daily_goals = {
    "water": 8, # cups
    "exercise": 30, # minutes
    "sleep": 7 # hours
}

# Store multiple entries for each habit
habits_data = {
    "water": [],
    "exercise": [],
    "sleep": []
}

# Tuple containing the habits the tracker supports
HABIT_NAMES = ("water", "exercise", "sleep")

print("=== Healthy Habits Tracker ===")
print("Track your progress toward today's healthy habit goals.")
print("Type 'done' when you are finished.\n")

while True:
    habit_choice = input(
        "Choose a habit (water / exercise / sleep) or 'done': "
    ).lower()

    # Exit the tracker when the user is finished
    if habit_choice == "done":
        break

    # Check whether the selected habit is supported
    elif habit_choice in HABIT_NAMES:
        try:
            user_value = float(
                input(f"Enter your {habit_choice} amount: ")
            )

            # Reject negative values
            if user_value < 0:
                print("Please enter a positive value.")
                continue

            # Sleep cannot realistically exceed 24 hours
            if habit_choice == "sleep" and user_value > 24:
                print("Sleep cannot exceed 24 hours in a day.")
                continue

            # Add the new entry to the appropriate habit list
            habits_data[habit_choice].append(user_value)

            # Calculate the accumulated amount for this habit
            current_total = sum(habits_data[habit_choice])
            daily_goal = daily_goals[habit_choice]

            print(
                f"You have logged {current_total:g} "
                f"for {habit_choice} today."
            )

            # Check whether the accumulated total reached the goal
            if current_total >= daily_goal:
                print(
                    f"Great job! You have reached your "
                    f"{habit_choice} goal."
                )
            else:
                remaining = daily_goal - current_total
                print(
                    f"Keep going! You need {remaining:g} more "
                    f"to reach your {habit_choice} goal."
                )

            print()

        # Handle input that cannot be converted to a number
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    # Handle an unsupported habit name
    else:
        print("That habit is not available. Please choose water, "
              "exercise, or sleep.\n")

# Display the final results
print("\n=== Today's Summary ===")

completed_habits = 0

for habit in HABIT_NAMES:
    entries = habits_data[habit]
    total = sum(entries)
    goal = daily_goals[habit]

    print(f"{habit.capitalize()}: {total:g} / {goal:g}")

    if total >= goal:
        print("Status: Goal reached!")
        completed_habits += 1
    else:
        print("Status: Goal not reached yet.")

    print(f"Entries recorded: {len(entries)}")
    print()

print(
    f"You completed {completed_habits} "
    f"out of {len(HABIT_NAMES)} daily goals."
)

print("Thanks for using the Healthy Habits Tracker!")
