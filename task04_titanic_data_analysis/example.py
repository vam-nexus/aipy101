"""
Concept: Titanic Data Analysis & Visualization

This example demonstrates analyzing real-world data using pandas and matplotlib.
Students will learn about data loading, grouping, aggregation, and creating meaningful visualizations.
"""

# Task 4 - Titanic Data Analysis & Visualization (Example File)
# This file demonstrates loading and basic analysis of the Titanic dataset

import pandas as pd
import matplotlib.pyplot as plt
import os

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Load the Titanic dataset
titanic_data = pd.read_csv(
    "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
)

# Quick look at the data
print("Dataset shape:", titanic_data.shape)
print("\nFirst 5 rows:")
print(titanic_data.head())

# Basic data analysis (Uncomment Below)
# -------------------------------------------
# print("\nDataset info:")
# print(titanic_data.info())
#
# print("\nBasic statistics:")
# print(titanic_data.describe())
#
# print("\nSurvival rate overall:")
# overall_survival = titanic_data["Survived"].mean()
# print(f"Overall survival rate: {overall_survival:.2%}")

# Calculate survival rate by gender (Uncomment Below)
# -------------------------------------------
# survival_by_gender = titanic_data.groupby("Sex")["Survived"].mean()
# print("\nSurvival rate by gender:")
# print(survival_by_gender)

# Calculate survival rate by passenger class (Uncomment Below)
# -------------------------------------------
# survival_by_class = titanic_data.groupby("Pclass")["Survived"].mean()
# print("\nSurvival rate by passenger class:")
# print(survival_by_class)

# Calculate average age of survivors and non-survivors (Uncomment Below)
# -------------------------------------------
# avg_age = titanic_data.groupby("Survived")["Age"].mean()
# print("\nAverage age by survival status:")
# print(avg_age)

# Create basic visualizations (Uncomment Below)
# -------------------------------------------
# # Bar chart of survival rate by gender
# survival_by_gender.plot(kind="bar", title="Survival Rate by Gender")
# plt.ylabel("Survival Rate")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.savefig("outputs/survival_by_gender.jpg")
# plt.close()
# print("Saved: outputs/survival_by_gender.jpg")

# Bar chart of survival rate by passenger class (Uncomment Below)
# -------------------------------------------
# survival_by_class.plot(kind="bar", title="Survival Rate by Passenger Class")
# plt.ylabel("Survival Rate")
# plt.xlabel("Passenger Class")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.savefig("outputs/survival_by_class.jpg")
# plt.close()
# print("Saved: outputs/survival_by_class.jpg")

# Histogram of ages for survivors vs. non-survivors (Uncomment Below)
# -------------------------------------------
# plt.figure(figsize=(10, 6))
# titanic_data[titanic_data["Survived"] == 1]["Age"].plot(kind="hist", alpha=0.5, label="Survived", bins=20)
# titanic_data[titanic_data["Survived"] == 0]["Age"].plot(kind="hist", alpha=0.5, label="Did Not Survive", bins=20)
# plt.legend()
# plt.title("Age Distribution by Survival")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.tight_layout()
# plt.savefig("outputs/age_distribution_by_survival.jpg")
# plt.close()
# print("Saved: outputs/age_distribution_by_survival.jpg")

# Advanced analysis examples (Uncomment Below)
# -------------------------------------------
# # Cross-tabulation of survival by class and gender
# crosstab = pd.crosstab([titanic_data["Pclass"], titanic_data["Sex"]], titanic_data["Survived"], normalize="index")
# print("\nSurvival rate by class and gender:")
# print(crosstab)
#
# # Create a more detailed visualization
# fig, axes = plt.subplots(2, 2, figsize=(15, 10))
#
# # Plot 1: Survival by gender
# survival_by_gender.plot(kind="bar", ax=axes[0,0], title="Survival Rate by Gender")
# axes[0,0].set_ylabel("Survival Rate")
# axes[0,0].tick_params(axis='x', rotation=0)
#
# # Plot 2: Survival by class
# survival_by_class.plot(kind="bar", ax=axes[0,1], title="Survival Rate by Class")
# axes[0,1].set_ylabel("Survival Rate")
# axes[0,1].tick_params(axis='x', rotation=0)
#
# # Plot 3: Age distribution
# titanic_data[titanic_data["Survived"] == 1]["Age"].plot(kind="hist", alpha=0.5, label="Survived", bins=20, ax=axes[1,0])
# titanic_data[titanic_data["Survived"] == 0]["Age"].plot(kind="hist", alpha=0.5, label="Did Not Survive", bins=20, ax=axes[1,0])
# axes[1,0].set_title("Age Distribution by Survival")
# axes[1,0].set_xlabel("Age")
# axes[1,0].legend()
#
# # Plot 4: Passenger distribution by class and gender
# pd.crosstab(titanic_data["Pclass"], titanic_data["Sex"]).plot(kind="bar", stacked=True, ax=axes[1,1])
# axes[1,1].set_title("Passenger Distribution by Class and Gender")
# axes[1,1].set_xlabel("Passenger Class")
# axes[1,1].tick_params(axis='x', rotation=0)
#
# plt.tight_layout()
# plt.savefig("outputs/comprehensive_analysis.jpg")
# plt.close()
# print("Saved: outputs/comprehensive_analysis.jpg")
