import IPython.display as display


def notebook_content():
    return """
# 🐍 Python Fundamentals: Hands-on Exercises


## Introduction
- Welcome to this interactive Python notebook!
- In this series of exercises, you'll write your first lines of Python code and explore core programming concepts.
- Each section includes a **Try This** explanation followed by a **Task** for you to complete.

## Submission Instructions
- Fill in the code for each exercise under the **Task** section.
- Perform the Challenge that is Exercise 31.
- Once completed, share a publicly viewable link to your Colab notebook in the submissions Excel sheet.

---

## Exercise 1: Print Statements

Printing in Python allows us to display text or values. It is useful for 
outputting messages, debugging, and formatting output for users.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.


### 🔹 Try This
Python's `print()` function outputs text. Example:
```python
print("Hello, world!")
```

### 🎯 Task: Print a Greeting
Use `print()` to display a greeting message of your choice.

```python
# Your code here
```

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

---

## Exercise 2: Variables

Variables store values in Python, making it easy to reuse and manipulate 
data throughout a program. They can hold numbers, text, or more complex 
structures.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
A variable stores data:
```python
name = "Alice"
print(name)
```

### 🎯 Task: Create and Print a Variable
Create a variable `city` and assign your favorite city to it, then print it.

```markdown
# Write your code below:
```

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

---

## Exercise 3: Data Types

Python supports multiple data types, including integers, floats, and 
strings. Understanding data types helps in performing appropriate 
operations on variables.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Python has different data types:
```python
x = 10       # Integer
y = 3.14     # Float
z = "Hello"  # String
```

### 🎯 Task: Create and Check Data Types
Create three variables: an integer, a float, and a string, and use `type()` to check them.

```python
# Your code here
```

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

---

## Exercise 4: Basic Arithmetic

Python can handle basic mathematical operations like addition, subtraction, 
multiplication, and division. These are essential for calculations in 
programming.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
You can perform math operations:
```python
sum = 5 + 3
product = 4 * 7
```

### 🎯 Task: Calculate Perimeter
Define variables `length` and `width`, then compute the perimeter of a rectangle.

```markdown
# Write your code below:
```

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

---

## Exercise 5: String Manipulation

Strings in Python can be combined, modified, and formatted using various 
methods. String operations are useful for text-based applications.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Strings can be combined and modified:
```python
greeting = "Hello" + " " + "Alice"
print(greeting)
```

### 🎯 Task: Combine Strings
Ask for the user's first and last name and print a full name using `input()`.

```python
# Your code here
```

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

---

## Exercise 6: Lists

Lists allow you to store multiple values in a single variable. They are 
useful for managing collections of related data efficiently.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Lists store multiple values:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
```

### 🎯 Task: Access List Elements
Create a list of three favorite foods and print the first one.

```markdown
# Write your code below:
```

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

---

## Exercise 7: If Statements

Conditional statements allow your program to make decisions. By checking 
conditions, Python can execute different code blocks based on the situation.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Conditional statements check conditions:
```python
if x > 0:
    print("Positive number")
```

### 🎯 Task: Check Positive or Negative
Write a program that checks if a number is positive or negative.

```python
# Your code here
```

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

---

## Exercise 8: Loops

Loops let you repeat actions multiple times. They are useful for iterating 
over data or running code until a condition is met.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Loops repeat actions:
```python
for i in range(5):
    print(i)
```

### 🎯 Task: Print Odd Numbers
Print odd numbers from 1 to 9 using a loop.

```markdown
# Write your code below:
```

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

---

## Exercise 9: Functions

Functions allow you to organize and reuse code efficiently. They take input, 
process it, and return a result, making programs more modular and readable.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Functions allow reusability:
```python
def greet(name):
    return "Hello " + name
print(greet("Alice"))
```

### 🎯 Task: Define a Function to Cube
Write a function that takes a number and returns its cube.

```python
# Your code here
```

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

---

## Exercise 10: Dictionaries

Dictionaries store data in key-value pairs, allowing for efficient data retrieval.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Dictionaries use key-value pairs:
```python
person = {"name": "Alice", "age": 25}
print(person["name"])
```

### 🎯 Task: Access Dictionary Values
Create a dictionary with three key-value pairs and print one of the keys.

```python
# Your code here
```

---

## Exercise 11: Sets

Sets are collections of unique elements, useful for membership testing and eliminating duplicates.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Sets store unique values:
```python
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)
```

### 🎯 Task: Demonstrate Set Uniqueness
Create a set of colors and demonstrate adding a duplicate color.

```python
# Your code here
```

---

## Exercise 12: Tuples

Tuples are immutable sequences, often used to store related data.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Tuples are immutable:
```python
coordinates = (10, 20)
print(coordinates[0])
```

### 🎯 Task: Access Tuple Elements
Create a tuple with three elements and print the first one.

```python
# Your code here
```

---

## Exercise 13: List Comprehensions

List comprehensions provide a concise way to create lists.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
List comprehensions simplify list creation:
```python
squares = [x**2 for x in range(5)]
print(squares)
```

### 🎯 Task: Create a List of Squares
Create a list of squares of numbers from 0 to 4 using list comprehension.

```python
# Your code here
```

---

## Exercise 14: File I/O

Python can read from and write to files, enabling data persistence.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Reading and writing files:
```python
with open("example.txt", "w") as file:
    file.write("Hello, world!")
```

### 🎯 Task: Read from a File
Write a program that reads a list of numbers from a file and prints them.

```python
# Your code here
```

---

## Exercise 15: Exception Handling

Exception handling allows you to manage errors gracefully.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Handle exceptions with try-except:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 🎯 Task: Handle a ValueError
Write a program that handles a ValueError when converting a string to an integer.

```python
# Your code here
```

---

## Exercise 16: NumPy Basics

NumPy is a powerful library for numerical computations.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
NumPy arrays for numerical operations:
```python
import numpy as np
array = np.array([1, 2, 3])
print(array + 1)
```

### 🎯 Task: Perform Array Operations
Create a NumPy array and perform a subtraction operation on it.

```python
# Your code here
```

---

## Exercise 17: Matplotlib Basics

Matplotlib is a library for creating static, interactive, and animated visualizations.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Plotting with Matplotlib:
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

### 🎯 Task: Plot a Bar Graph
Use Matplotlib to plot a simple bar graph.

```python
# Your code here
```

---

## Exercise 18: Pandas Basics

Pandas is a library for data manipulation and analysis.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Data manipulation with Pandas:
```python
import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)
```

### 🎯 Task: Manipulate a DataFrame
Create a Pandas DataFrame and add a new column to it.

```python
# Your code here
```

---

## Exercise 19: Random Module

The random module is used to generate random numbers.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Generate random numbers:
```python
import random
print(random.randint(1, 10))
```

### 🎯 Task: Generate a Random Float
Write a program that generates a random float between 0 and 1.

```python
# Your code here
```

---

## Exercise 20: Time Module

The time module provides various time-related functions.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Use the time module:
```python
import time
print(time.ctime())
```

### 🎯 Task: Delay Execution
Write a program that delays execution for 2 seconds and then prints a message.

```python
# Your code here
```

---

## Exercise 21: Function with Multiple Parameters

Functions can take multiple parameters to perform operations on them.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Define a function with multiple parameters:
```python
def add(a, b):
    return a + b
print(add(3, 4))
```

### 🎯 Task: Create a Function to Multiply
Write a function that takes two numbers and returns their product.

```python
# Your code here
```

---

## Exercise 22: Default Parameters

Functions can have default parameter values, which are used if no argument is provided.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Define a function with a default parameter:
```python
def greet(name="Guest"):
    return "Hello " + name
print(greet())
```

### 🎯 Task: Create a Function with Default Value
Write a function that greets a user with a default name if no name is provided.

```python
# Your code here
```

---

## Exercise 23: Return Multiple Values

Functions can return multiple values using tuples.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Return multiple values from a function:
```python
def get_coordinates():
    return (10, 20)
x, y = get_coordinates()
print(x, y)
```

### 🎯 Task: Create a Function to Return Multiple Values
Write a function that returns the sum and product of two numbers.

```python
# Your code here
```

---

## Exercise 24: Recursive Functions

A recursive function is a function that calls itself to solve a problem.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Define a recursive function:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
```

### 🎯 Task: Create a Recursive Function
Write a recursive function to calculate the Fibonacci sequence.

```python
# Your code here
```

---

## Exercise 25: Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Define a lambda function:
```python
square = lambda x: x * x
print(square(5))
```

### 🎯 Task: Create a Lambda Function
Write a lambda function to add two numbers.

```python
# Your code here
```

---

## Exercise 26: DataFrame Filtering

Filtering allows you to select specific rows based on conditions.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Filter a DataFrame:
```python
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
filtered_df = df[df['Age'] > 30]
print(filtered_df)
```

### 🎯 Task: Filter DataFrame by Multiple Conditions
Create a DataFrame with columns for 'Name', 'Age', and 'City'. Filter the DataFrame to show only rows where 'Age' is greater than 25 and 'City' is 'New York'.

```python
# Your code here
```

---

## Exercise 27: Grouping and Aggregation

Grouping and aggregation allow you to summarize data.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Group and aggregate data:
```python
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Alice'], 'Score': [85, 90, 95]}
df = pd.DataFrame(data)
grouped = df.groupby('Name').mean()
print(grouped)
```

### 🎯 Task: Group and Aggregate with Multiple Functions
Create a DataFrame with 'Name', 'Score', and 'Attempts'. Group by 'Name' and calculate both the mean and sum of 'Score' for each group.

```python
# Your code here
```

---

## Exercise 28: DataFrame Merging

Merging combines data from multiple DataFrames.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Merge DataFrames:
```python
import pandas as pd
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
df2 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Score': [85, 90]})
merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)
```

### 🎯 Task: Merge with Different Join Types
Create two DataFrames with some overlapping and some unique 'Name' entries. Merge them using an outer join and display the result.

```python
# Your code here
```

---

## Exercise 29: Plotting with Pandas

Pandas can be used to plot data directly.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Plot data with Pandas:
```python
import pandas as pd
import matplotlib.pyplot as plt
data = {'Year': [2010, 2011, 2012], 'Sales': [200, 250, 300]}
df = pd.DataFrame(data)
df.plot(x='Year', y='Sales', kind='line')
plt.show()
```

### 🎯 Task: Plot Multiple Lines
Create a DataFrame with 'Year', 'Product_A_Sales', and 'Product_B_Sales'. Plot both sales lines on the same graph with different colors.

```python
# Your code here
```

---

## Exercise 30: Advanced Plotting with Matplotlib

Create complex plots using Matplotlib.

💡 **Tip:** You can always consult ChatGPT to explain the code and help you with the task.

### 🔹 Try This
Create a subplot:
```python
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2)
axs[0].plot([1, 2, 3], [4, 5, 6])
axs[1].bar([1, 2, 3], [4, 5, 6])
plt.show()
```

### 🎯 Task: Create a Complex Subplot
Use Matplotlib to create a 2x2 subplot grid. Include a line plot, a bar plot, a scatter plot, and a histogram, each in a different subplot.

```python
# Your code here
```

---

## Exercise 31: Titanic Data Analysis Challenge

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

```python
# Your code here
```

---

### 🎉 Congratulations! You've completed Python Fundamentals exercises!
    """


display.Markdown(notebook_content())
