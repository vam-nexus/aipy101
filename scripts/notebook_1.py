import nbformat as nbf

# Create a new notebook
nb = nbf.v4.new_notebook()

# Define the content for each cell
cells = [
    nbf.v4.new_markdown_cell(
        """
# 🐍 Python Fundamentals: Hands-on Exercises

## Introduction
- Welcome to this interactive Python notebook!
- In this series of exercises, you'll write your first lines of Python code and explore core programming concepts.
- Each section includes a **Try This** explanation followed by a **Task** for you to complete.

## Submission Instructions
- Fill in the code for each exercise under the **Task** section.
- Perform the Challenge that is Exercise 31.
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 1: Print Statements

Printing in Python allows us to display text or values. It is useful for 
outputting messages, debugging, and formatting output for users.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
print("Hello, world!")
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Print a Greeting
Use `print()` to display a greeting message of your choice.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 2: Variables

Variables store values in Python, making it easy to reuse and manipulate 
data throughout a program. They can hold numbers, text, or more complex 
structures.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
name = "Alice"
print(name)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Create and Print a Variable
Create a variable `city` and assign your favorite city to it, then print it.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 3: Data Types

Python supports multiple data types, including integers, floats, and 
strings. Understanding data types helps in performing appropriate 
operations on variables.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
x = 10       # Integer
y = 3.14     # Float
z = "Hello"  # String
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Create and Check Data Types
Create three variables: an integer, a float, and a string, and use `type()` to check them.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 4: Basic Arithmetic

Python can handle basic mathematical operations like addition, subtraction, 
multiplication, and division. These are essential for calculations in 
programming.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
sum = 5 + 3
product = 4 * 7
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Calculate Perimeter
Define variables `length` and `width`, then compute the perimeter of a rectangle.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    # Additional exercises in a similar format
    nbf.v4.new_markdown_cell(
        """
## Exercise 5: String Manipulation

Strings in Python can be combined, modified, and formatted using various 
methods. String operations are useful for text-based applications.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
greeting = "Hello" + " " + "Alice"
print(greeting)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Combine Strings
Ask for the user's first and last name and print a full name using `input()`.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 6: Lists

Lists allow you to store multiple values in a single variable. They are 
useful for managing collections of related data efficiently.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Access List Elements
Create a list of three favorite foods and print the first one.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 7: If Statements

Conditional statements allow your program to make decisions. By checking 
conditions, Python can execute different code blocks based on the situation.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
if x > 0:
    print("Positive number")
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Check Positive or Negative
Write a program that checks if a number is positive or negative.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    # Add Exercise 8: Loops
    nbf.v4.new_markdown_cell(
        """
## Exercise 8: Loops

Loops let you repeat actions multiple times. They are useful for iterating 
over data or running code until a condition is met.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
for i in range(5):
    print(i)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Print Odd Numbers
Print odd numbers from 1 to 9 using a loop.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Write your code below:
"""
    ),
    # Add Exercise 9: Functions
    nbf.v4.new_markdown_cell(
        """
## Exercise 9: Functions

Functions allow you to organize and reuse code efficiently. They take input, 
process it, and return a result, making programs more modular and readable.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
def greet(name):
    return "Hello " + name
print(greet("Alice"))
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Define a Function to Cube
Write a function that takes a number and returns its cube.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    # Add Exercise 10: Dictionaries
    nbf.v4.new_markdown_cell(
        """
## Exercise 10: Dictionaries

Dictionaries store data in key-value pairs, allowing for efficient data retrieval.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
person = {"name": "Alice", "age": 25}
print(person["name"])
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Access Dictionary Values
Create a dictionary with three key-value pairs and print one of the keys.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    # Add Exercise 11: Sets
    nbf.v4.new_markdown_cell(
        """
## Exercise 11: Sets

Sets are collections of unique elements, useful for membership testing and eliminating duplicates.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Demonstrate Set Uniqueness
Create a set of colors and demonstrate adding a duplicate color.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    # Add Exercise 12: Tuples
    nbf.v4.new_markdown_cell(
        """
## Exercise 12: Tuples

Tuples are immutable sequences, often used to store related data.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
coordinates = (10, 20)
print(coordinates[0])
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Access Tuple Elements
Create a tuple with three elements and print the first one.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    # Add Exercise 13: List Comprehensions
    nbf.v4.new_markdown_cell(
        """
## Exercise 13: List Comprehensions

List comprehensions provide a concise way to create lists.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
squares = [x**2 for x in range(5)]
print(squares)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Create a List of Squares
Create a list of squares of numbers from 0 to 4 using list comprehension.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    # Add Exercise 14: File I/O
    nbf.v4.new_markdown_cell(
        """
## Exercise 14: File I/O

Python can read from and write to files, enabling data persistence.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
with open("example.txt", "w") as file:
    file.write("Hello, world!")
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Read from a File
Write a program that reads a list of numbers from a file and prints them.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    # Add Exercise 15: Exception Handling
    nbf.v4.new_markdown_cell(
        """
## Exercise 15: Exception Handling

Exception handling allows you to manage errors gracefully.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Handle a ValueError
Write a program that handles a ValueError when converting a string to an integer.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 16: NumPy Basics

NumPy is a powerful library for numerical computations.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
"""
    ),
    nbf.v4.new_code_cell(
        """
import numpy as np
array = np.array([1, 2, 3])
print(array + 1)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Perform Array Operations
Create a NumPy array and perform a subtraction operation on it.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 17: Matplotlib Basics

Matplotlib is a library for creating static, interactive, and animated visualizations.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Plotting with Matplotlib:
"""
    ),
    nbf.v4.new_code_cell(
        """
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Plot a Bar Graph
Use Matplotlib to plot a simple bar graph.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 18: Pandas Basics

Pandas is a library for data manipulation and analysis.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Data manipulation with Pandas:
"""
    ),
    nbf.v4.new_code_cell(
        """
import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Manipulate a DataFrame
Create a Pandas DataFrame and add a new column to it.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 19: Random Module

The random module is used to generate random numbers.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Generate random numbers:
"""
    ),
    nbf.v4.new_code_cell(
        """
import random
print(random.randint(1, 10))
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Generate a Random Float
Write a program that generates a random float between 0 and 1.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 20: Time Module

The time module provides various time-related functions.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Use the time module:
"""
    ),
    nbf.v4.new_code_cell(
        """
import time
print(time.ctime())
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Delay Execution
Write a program that delays execution for 2 seconds and then prints a message.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 21: Function with Multiple Parameters

Functions can take multiple parameters to perform operations on them.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Define a function with multiple parameters:
"""
    ),
    nbf.v4.new_code_cell(
        """
def add(a, b):
    return a + b
print(add(3, 4))
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Create a Function to Multiply
Write a function that takes two numbers and returns their product.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 22: Default Parameters

Functions can have default parameter values, which are used if no argument is provided.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Define a function with a default parameter:
"""
    ),
    nbf.v4.new_code_cell(
        """
def greet(name="Guest"):
    return "Hello " + name
print(greet())
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Create a Function with Default Value
Write a function that greets a user with a default name if no name is provided.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 23: Return Multiple Values

Functions can return multiple values using tuples.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Return multiple values from a function:
"""
    ),
    nbf.v4.new_code_cell(
        """
def get_coordinates():
    return (10, 20)
x, y = get_coordinates()
print(x, y)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Create a Function to Return Multiple Values
Write a function that returns the sum and product of two numbers.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 24: Recursive Functions

A recursive function is a function that calls itself to solve a problem.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Define a recursive function:
"""
    ),
    nbf.v4.new_code_cell(
        """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Create a Recursive Function
Write a recursive function to calculate the Fibonacci sequence.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 25: Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Define a lambda function:
"""
    ),
    nbf.v4.new_code_cell(
        """
square = lambda x: x * x
print(square(5))
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Create a Lambda Function
Write a lambda function to add two numbers.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 26: DataFrame Filtering

Filtering allows you to select specific rows based on conditions.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Filter a DataFrame:
"""
    ),
    nbf.v4.new_code_cell(
        """
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
filtered_df = df[df['Age'] > 30]
print(filtered_df)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Filter DataFrame by Multiple Conditions
Create a DataFrame with columns for 'Name', 'Age', and 'City'. Filter the DataFrame to show only rows where 'Age' is greater than 25 and 'City' is 'New York'.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 27: Grouping and Aggregation

Grouping and aggregation allow you to summarize data.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Group and aggregate data:
"""
    ),
    nbf.v4.new_code_cell(
        """
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Alice'], 'Score': [85, 90, 95]}
df = pd.DataFrame(data)
grouped = df.groupby('Name').mean()
print(grouped)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Group and Aggregate with Multiple Functions
Create a DataFrame with 'Name', 'Score', and 'Attempts'. Group by 'Name' and calculate both the mean and sum of 'Score' for each group.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 28: DataFrame Merging

Merging combines data from multiple DataFrames.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Merge DataFrames:
"""
    ),
    nbf.v4.new_code_cell(
        """
import pandas as pd
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
df2 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Score': [85, 90]})
merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Merge with Different Join Types
Create two DataFrames with some overlapping and some unique 'Name' entries. Merge them using an outer join and display the result.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 29: Plotting with Pandas

Pandas can be used to plot data directly.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Plot data with Pandas:
"""
    ),
    nbf.v4.new_code_cell(
        """
import pandas as pd
import matplotlib.pyplot as plt
data = {'Year': [2010, 2011, 2012], 'Sales': [200, 250, 300]}
df = pd.DataFrame(data)
df.plot(x='Year', y='Sales', kind='line')
plt.show()
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Plot Multiple Lines
Create a DataFrame with 'Year', 'Product_A_Sales', and 'Product_B_Sales'. Plot both sales lines on the same graph with different colors.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 30: Advanced Plotting with Matplotlib

Create complex plots using Matplotlib.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Create a subplot:
"""
    ),
    nbf.v4.new_code_cell(
        """
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2)
axs[0].plot([1, 2, 3], [4, 5, 6])
axs[1].bar([1, 2, 3], [4, 5, 6])
plt.show()
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Create a Complex Subplot
Use Matplotlib to create a 2x2 subplot grid. Include a line plot, a bar plot, a scatter plot, and a histogram, each in a different subplot.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 31: Saving and Loading CSV Files

CSV files are a common format for storing tabular data. Python's Pandas library makes it easy to read from and write to CSV files.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Save and load a DataFrame to/from a CSV file:
"""
    ),
    nbf.v4.new_code_cell(
        """
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('people.csv', index=False)

# Load from CSV
loaded_df = pd.read_csv('people.csv')
print(loaded_df)
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎯 Task: Save and Load Your Data
1. **Create a DataFrame**: Create a DataFrame with columns 'Product', 'Price', and 'Quantity'.
2. **Save to CSV**: Save the DataFrame to a CSV file named `inventory.csv`.
3. **Load from CSV**: Load the data back into a new DataFrame and print it.
4. **View the CSV**: Open the `inventory.csv` file in a text editor or spreadsheet application to view its contents.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
## Exercise 32: Titanic Data Analysis Challenge

In this challenge, you'll work with the Titanic dataset to perform data cleaning and analysis using Pandas.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Download the Titanic dataset from Kaggle:
1. Visit [Kaggle Titanic Competition](https://www.kaggle.com/competitions/titanic/data).
2. Download the `train.csv` file.

### 🎯 Task: Analyze the Titanic Dataset
1. **Upload the CSV**: Load the `train.csv` file into a Pandas DataFrame.
2. **Clean the Data**: Remove rows with missing values (NaNs).
3. **Analyze the Data**:
   - Calculate the survival rate by gender.
   - Calculate the survival rate by passenger class.
   - Calculate the average age of survivors and non-survivors.
4. **Visualize the Data**:
   - Plot the survival rate by gender using a bar chart.
   - Plot the survival rate by passenger class using a bar chart.
   - Create a histogram of ages for survivors and non-survivors.
5. **Explore Further**:
   - Plot two additional interesting insights you discover from the dataset.
"""
    ),
    nbf.v4.new_code_cell(
        """
# Your code here
"""
    ),
    nbf.v4.new_markdown_cell(
        """
### 🎉 Congratulations! You've completed Python Fundamentals exercises!
"""
    ),
]

# Assign cells to the notebook
nb.cells.extend(cells)

# Save the notebook
with open("python_fundamentals.ipynb", "w") as f:
    nbf.write(nb, f)
