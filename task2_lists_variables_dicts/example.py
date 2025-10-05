"""
Concept: Lists, Variables & Dicts

This example demonstrates working with dictionaries, lists, and variables.
Students will learn about mutable data structures, iteration, and data formatting.
"""

# Task 2 - Lists, Variables & Dicts (Example File)
# This file demonstrates building and editing a profile dictionary

# Create a basic profile dictionary
profile = {
    "name": "Alice Johnson",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "hiking", "cooking"],
}

print("Original profile:")
print(profile)

# Access dictionary values (Uncomment Below)
# -------------------------------------------
# print(f"\nName: {profile['name']}")
# print(f"Age: {profile['age']}")
# print(f"City: {profile['city']}")

# Modify existing values (Uncomment Below)
# -------------------------------------------
# profile["age"] = 26
# profile["city"] = "San Francisco"
#
# print(f"\nAfter modifications:")
# print(f"Updated age: {profile['age']}")
# print(f"Updated city: {profile['city']}")

# Add new key-value pairs (Uncomment Below)
# -------------------------------------------
# profile["email"] = "alice.johnson@email.com"
# profile["occupation"] = "Software Developer"
#
# print(f"\nAfter adding new fields:")
# print(profile)

# Work with lists in the dictionary (Uncomment Below)
# -------------------------------------------
# print(f"\nHobbies:")
# for hobby in profile["hobbies"]:
#     print(f"- {hobby}")

# Add a new hobby (Uncomment Below)
# -------------------------------------------
# profile["hobbies"].append("photography")
# print(f"\nAfter adding photography:")
# print(f"Hobbies: {profile['hobbies']}")

# Create a summary function (Uncomment Below)
# -------------------------------------------
# def summarize_profile(person):
#     """Create a formatted summary of a person's profile"""
#     summary = f"""
# === PROFILE SUMMARY ===
# Name: {person['name']}
# Age: {person['age']}
# Location: {person['city']}
# Email: {person['email']}
# Occupation: {person['occupation']}
# Hobbies: {', '.join(person['hobbies'])}
# ========================
# """
#     return summary

# Use the summary function (Uncomment Below)
# -------------------------------------------
# print(summarize_profile(profile))
