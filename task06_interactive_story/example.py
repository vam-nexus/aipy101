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
