# Lost Temple Adventure

import logging
from enum import Enum


# Symbolic values describe the player's progress through the adventure.
class GameState(Enum):
    TRAPPED = 0
    SEAL_FOUND = 1
    ESCAPED = 2


logging.basicConfig(
    filename="game_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Each main location contains three actions the explorer can investigate.
exploration_areas = {
    "1": {
        "name": "Stone Altar",
        "actions": {
            "1": "Read the worn altar inscription",
            "2": "Inspect the offering bowl",
            "3": "Move the stone brazier",
        },
    },
    "2": {
        "name": "Ancient Library",
        "actions": {
            "1": "Study the cracked history scrolls",
            "2": "Search behind the map cabinet",
            "3": "Climb the leaning bookcase",
        },
    },
    "3": {
        "name": "Underground Chamber",
        "actions": {
            "1": "Examine the underground carvings",
            "2": "Cross the shallow reflecting pool",
            "3": "Open the moss-covered stone chest",
        },
    },
}

inventory = {}
exploration_history = []
game_state = GameState.TRAPPED

print("=== Lost Temple Adventure ===")
print("You are an explorer trapped inside an ancient temple.")
print("Find the Ancient Seal and use it to open the sealed exit.\n")

while game_state != GameState.ESCAPED:
    try:
        print("\n=== Center of the Temple ===")
        print("Choose an action:")

        menu_options = {
            "1": "Explore the Stone Altar",
            "2": "Search the Ancient Library",
            "3": "Investigate the Underground Chamber",
            "4": "Approach the Sealed Exit",
            "5": "View Recent Exploration History",
            "0": "Quit the game",
        }

        # .items() lets us display every menu number and its description.
        for menu_number, menu_text in menu_options.items():
            print(f"{menu_number} - {menu_text}")

        user_input = input("\nYour choice: ").strip()
        choice = user_input[:1]

        # .keys() is used to validate the numbered main menu choices.
        if choice not in menu_options.keys():
            raise KeyError(choice)

        if choice == "0":
            print("You leave the temple mystery unsolved. Goodbye!")
            break

        elif choice in exploration_areas.keys():
            area = exploration_areas[choice]
            while True:
                print(f"\n=== {area['name']} ===")

                for action_number, action_text in area["actions"].items():
                    print(f"{action_number} - {action_text}")
                print("0 - Return to the center of the temple")

                try:
                    subaction_input = input("\nWhat do you investigate? ").strip()
                    subaction = subaction_input[:1]

                    if subaction == "0":
                        print("You return to the center of the temple.")
                        break

                    if subaction not in area["actions"].keys():
                        raise KeyError(subaction)

                    action_text = area["actions"][subaction]
                    exploration_history.append(f"{area['name']}: {action_text}")
                    print(f"\nYou {action_text.lower()}.")

                    # One action in each area reveals a different item or clue.
                    if choice == "1" and subaction == "3":
                        if inventory.get("healing_fruit", False):
                            print(
                                "The hidden compartment is empty. You already "
                                "took the Healing Fruit."
                            )
                        else:
                            print("A hidden compartment contains a Healing Fruit.")
                            inventory["healing_fruit"] = True
                            print("You place the Healing Fruit in your inventory.")
                    elif choice == "2" and subaction == "2":
                        if inventory.get("ancient_seal", False):
                            print("The map cabinet is empty. You already have the Ancient Seal.")
                        else:
                            print("Behind the cabinet, you discover the Ancient Seal!")
                            inventory["ancient_seal"] = True
                            game_state = GameState.SEAL_FOUND
                            print("The seal feels warm in your hand.")
                    elif choice == "3" and subaction == "3":
                        print("The chest is empty, but its lid bears a warning:")
                        print("'Only the seal may command the temple gate.'")
                    else:
                        print("You find clues about a sealed exit, but no useful item.")

                except KeyError as error:
                    logging.error("Invalid submenu selection: %s", error)
                    print("That is not a valid choice. Please choose 1, 2, 3, or 0.")

                except Exception as error:
                    logging.error("Unexpected submenu error: %s", error)
                    print("Something went wrong, but you can try this location again.")

        elif choice == "4":
            print("\nYou approach a towering door covered in golden symbols.")

            # .get() safely checks the inventory without a missing-key error.
            if inventory.get("ancient_seal", False):
                print("You press the Ancient Seal into the door.")
                print("The symbols blaze. The sealed exit opens to moonlight!")
                game_state = GameState.ESCAPED
            else:
                print("The exit is sealed. You need the Ancient Seal.")

        elif choice == "5":
            print("\n=== Recent Exploration History ===")
            recent_history = exploration_history[-3:]
            if recent_history:
                history_number = 1
                for history_text in recent_history:
                    print(f"{history_number}. {history_text}")
                    history_number += 1
            else:
                print("You have not explored any temple areas yet.")

    except KeyError as error:
        logging.error("Invalid menu selection: %s", error)
        print("That is not a valid choice. Please select one of the listed options.")

    except Exception as error:
        logging.error("Unexpected game error: %s", error)
        print("Something went wrong, but the temple gives you another chance.")

    finally:
        logging.info("Finished a main game-loop iteration; state=%s", game_state.name)

if game_state == GameState.ESCAPED:
    print("\n=== You Escaped! ===")
    print("You escaped the Lost Temple with the Ancient Seal. Well done!")
