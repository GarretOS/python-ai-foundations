# 🏛️ Lost Temple Adventure

Lost Temple Adventure is a beginner Python text adventure based on the TowardsAI lesson “Text Adventure Game.” You play as an explorer trapped inside an ancient temple. Explore its chambers, find the Ancient Seal, and use it to open the sealed exit.

## 🎯 Project Overview

The game presents a numbered main menu and smaller menus for three temple locations. One exploration action hides the Ancient Seal, another hides an optional Healing Fruit, and the sealed exit checks the player's inventory before allowing them to escape.

## ✨ Features

- Explore the Stone Altar, Ancient Library, and Underground Chamber through their own submenus
- Continue investigating a location until choosing `0` to return to the temple center
- Find the Ancient Seal required to win
- Discover an optional Healing Fruit
- View the three most recent exploration actions
- Accept inputs such as `2` or `2 library`
- Handle invalid menu choices without crashing
- Record game-loop activity and errors in the generated `game_log.txt`
- Use an Enum to track the adventure state

## 🐍 Python Concepts

- Variables, strings, lists, and dictionaries
- Nested dictionaries
- `for` and `while` loops
- `if`, `elif`, and `else` conditionals
- User input and string slicing
- List slicing with `exploration_history[-3:]`
- Dictionary `.items()`, `.keys()`, and `.get()`
- `try`, multiple `except` blocks, and `finally`
- Built-in logging
- `Enum`

## 📁 Project Structure

```text
lost-temple-adventure/
├── README.md
├── lost_temple_adventure.py
├── lost_temple_adventure.ipynb
└── requirements.txt
```

- `lost_temple_adventure.py` contains the complete game script.
- `lost_temple_adventure.ipynb` contains the notebook version for Jupyter or Google Colab.
- `requirements.txt` documents that no third-party dependencies are required.

## 🚀 How to Run

Python 3 is required. From this project directory, run:

```bash
python lost_temple_adventure.py
```

You can also open the notebook in Google Colab:

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/lost-temple-adventure/lost_temple_adventure.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 💡 Example Output

```text
=== Lost Temple Adventure ===
You are an explorer trapped inside an ancient temple.
Find the Ancient Seal and use it to open the sealed exit.

=== Center of the Temple ===
Choose an action:
1 - Explore the Stone Altar
2 - Search the Ancient Library
3 - Investigate the Underground Chamber
4 - Approach the Sealed Exit
5 - View Recent Exploration History
0 - Quit the game
```

## 📚 What I Learned

This project practices organizing a small game with nested dictionaries, tracking items in an inventory, repeating menu interactions with loops, validating choices, and using conditions to change the story. It also demonstrates dictionary methods, slicing, exception handling, logging, and an Enum while staying within Python's built-in features.

## 📝 Notes

- The temple, items, and story are fictional.
- Exploration history and inventory last only for the current program session.
- `game_log.txt` is generated while the game runs in the directory where the script is run. It is not a source file and should not be committed.
