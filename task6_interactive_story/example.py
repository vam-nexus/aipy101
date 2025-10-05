"""
Concept: Interactive Story

This example demonstrates input/output, conditionals, and basic user interaction.
Students will learn about user input, string formatting, and control flow in interactive programs.
"""

# Task 6 - Interactive Story (Example File)
# This file demonstrates creating an interactive story


def story():
    """Basic interactive story with user input"""
    name = input("Hero, what's your name? ")
    path = input("Left or Right? ")
    print(f"{name} chose {path} and found treasure!")
    print("The end!")


# Run the basic story
story()

# Enhanced story with more choices (Uncomment Below)
# -------------------------------------------
# def enhanced_story():
#     """Enhanced story with multiple choices and outcomes"""
#     print("=== Welcome to the Adventure! ===")
#     name = input("Hero, what's your name? ")
#     print(f"Welcome, {name}! Your adventure begins...")
#
#     # First choice
#     print("\nYou come to a fork in the road.")
#     path = input("Do you go Left or Right? ").lower()
#
#     if path == "left":
#         print(f"{name} chose left and found a magical sword!")
#         weapon = "magical sword"
#     elif path == "right":
#         print(f"{name} chose right and found a healing potion!")
#         weapon = "healing potion"
#     else:
#         print(f"{name} hesitated and found nothing...")
#         weapon = "nothing"
#
#     # Second choice
#     print(f"\nYou now have a {weapon}.")
#     action = input("Do you want to Fight or Explore? ").lower()
#
#     if action == "fight" and weapon == "magical sword":
#         print(f"{name} bravely fought and defeated the dragon!")
#         print("You are victorious!")
#     elif action == "explore":
#         print(f"{name} explored further and discovered a hidden village!")
#         print("The villagers welcome you as a hero!")
#     else:
#         print(f"{name} was not prepared and had to retreat...")
#         print("Better luck next time!")
#
#     print(f"\nThanks for playing, {name}!")

# enhanced_story()

# Story with inventory system (Uncomment Below)
# -------------------------------------------
# def story_with_inventory():
#     """Story with inventory management"""
#     print("=== Adventure with Inventory ===")
#     name = input("Hero, what's your name? ")
#     inventory = []
#
#     print(f"Welcome, {name}! You start with an empty backpack.")
#     print(f"Inventory: {inventory}")
#
#     # First choice
#     print("\nYou find a chest. Do you open it?")
#     choice = input("Yes or No? ").lower()
#
#     if choice == "yes":
#         item = "gold coins"
#         inventory.append(item)
#         print(f"You found {item}!")
#         print(f"Inventory: {inventory}")
#     else:
#         print("You leave the chest unopened.")
#
#     # Second choice
#     print("\nA merchant offers to trade. Do you accept?")
#     trade = input("Yes or No? ").lower()
#
#     if trade == "yes" and "gold coins" in inventory:
#         inventory.remove("gold coins")
#         inventory.append("magic potion")
#         print("You traded gold coins for a magic potion!")
#         print(f"Inventory: {inventory}")
#     elif trade == "yes":
#         print("You have nothing to trade!")
#     else:
#         print("You decline the trade.")
#
#     print(f"\nFinal inventory: {inventory}")
#     print(f"Thanks for playing, {name}!")

# story_with_inventory()

# Story with file logging (Uncomment Below)
# -------------------------------------------
# def story_with_logging():
#     """Story that saves choices to a file"""
#     import datetime
#
#     print("=== Adventure with Logging ===")
#     name = input("Hero, what's your name? ")
#     log_entries = []
#
#     # Log the start
#     log_entries.append(f"{datetime.datetime.now()}: {name} started their adventure")
#
#     # First choice
#     print("\nYou encounter a mysterious door.")
#     choice = input("Do you knock or walk away? ").lower()
#     log_entries.append(f"{datetime.datetime.now()}: {name} chose to {choice}")
#
#     if choice == "knock":
#         print("The door opens to reveal a friendly wizard!")
#         log_entries.append(f"{datetime.datetime.now()}: {name} met a friendly wizard")
#     else:
#         print("You walk away and find a different path.")
#         log_entries.append(f"{datetime.datetime.now()}: {name} found a different path")
#
#     # Save log to file
#     with open("adventure_log.txt", "w") as file:
#         for entry in log_entries:
#             file.write(entry + "\n")
#
#     print(f"\nYour adventure has been saved to 'adventure_log.txt'")
#     print(f"Thanks for playing, {name}!")

# story_with_logging()
