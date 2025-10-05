# Task 4 - Titanic Data Analysis & Visualization (Exercise File)
#
# 🧩 CHALLENGE: Create 3 Custom Plots (Extra Challenge)
#
# Requirements:
# - Create 3 additional custom plots of your choice, such as:
#   💠 Pie chart of passenger gender proportions
#   📊 Boxplot comparing ages across classes
#   📈 Stacked bar chart of survival rate by class and gender
#   📉 Scatter plot of age vs. fare colored by survival
#   📊 Heatmap of survival rates by class and gender
#   📈 Line plot showing survival rate trends by age groups
#   📊 Violin plot of fare distribution by survival status
# - Save each plot to the outputs/ folder with descriptive names
# - Each plot should tell a story about the data
# - Use creative titles and proper formatting
#
# 💡 TIP: You can use an AI assistant to help you with this task!
# Ask questions like:
# - "How do I create a pie chart with matplotlib?"
# - "How do I create a boxplot in pandas?"
# - "How do I create a heatmap with seaborn or matplotlib?"
# - "What's the best way to create a stacked bar chart?"
# - "How do I create a scatter plot with different colors for categories?"
#
# Your code goes here:
# TODO: Create your 3 custom plots below this line

import pandas as pd
import matplotlib.pyplot as plt
import os

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Load the Titanic dataset
titanic_data = pd.read_csv(
    "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
)
