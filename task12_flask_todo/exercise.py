# Task 12 - Flask Todo List (Exercise File)
#
# 🧩 CHALLENGE: Add advanced todo features
#
# Requirements:
# - Add task categories (work, personal, shopping, etc.)
# - Add due dates to tasks
# - Add task priority levels (high, medium, low)
# - Add search functionality to filter tasks
# - Add task editing functionality
#
# Advanced Features to Consider:
# - Task sorting (by date, priority, category)
# - Task filtering by status (completed, pending)
# - Bulk operations (delete multiple, mark multiple as complete)
# - Task notes/descriptions
# - Task sharing between users
#
# 💡 TIP: You can use an AI assistant to help you with this task!
# Ask questions like:
# - "How do I add categories to todo items in Flask?"
# - "How do I implement search functionality in a web app?"
# - "How do I add date pickers to HTML forms?"
# - "How do I create dropdown menus for priority levels?"
#
# Your code goes here:
# TODO: Add advanced todo features below this line

from flask import Flask, render_template, request, redirect, session
import json
import os

app = Flask(__name__)
app.secret_key = "supersecret"


# Load users from JSON file
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return [{"name": "admin", "password": "password"}]


def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)


def find_user(username):
    """Find user by username in the list"""
    for user in users:
        if user["name"] == username:
            return user
    return None


# Load todos from JSON file
def load_todos():
    if os.path.exists("todos.json"):
        with open("todos.json", "r") as f:
            return json.load(f)
    return {}


def save_todos(todos):
    with open("todos.json", "w") as f:
        json.dump(todos, f)


users = load_users()
todos = load_todos()


@app.route("/")
def index():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = find_user(username)
        if user and user["password"] == password:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if find_user(username):
            return render_template("signup.html", error="Username already exists")

        users.append({"name": username, "password": password})
        save_users(users)

        return redirect("/login?message=signup_success")

    return render_template("signup.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    username = session["user"]
    user_todos = todos.get(username, [])

    return render_template("dashboard.html", username=username, todos=user_todos)


@app.route("/add_todo", methods=["POST"])
def add_todo():
    if "user" not in session:
        return redirect("/login")

    username = session["user"]
    task = request.form["task"]

    if username not in todos:
        todos[username] = []

    todos[username].append(
        {"id": len(todos[username]) + 1, "task": task, "completed": False}
    )

    save_todos(todos)
    return redirect("/dashboard")


@app.route("/toggle_todo/<int:todo_id>")
def toggle_todo(todo_id):
    if "user" not in session:
        return redirect("/login")

    username = session["user"]
    if username in todos:
        for todo in todos[username]:
            if todo["id"] == todo_id:
                todo["completed"] = not todo["completed"]
                break
        save_todos(todos)

    return redirect("/dashboard")


@app.route("/delete_todo/<int:todo_id>")
def delete_todo(todo_id):
    if "user" not in session:
        return redirect("/login")

    username = session["user"]
    if username in todos:
        todos[username] = [todo for todo in todos[username] if todo["id"] != todo_id]
        save_todos(todos)

    return redirect("/dashboard")


# TODO: Add your advanced features here
# - Add task categories
# - Add due dates
# - Add priority levels
# - Add search functionality
# - Add task editing


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True, port=5012)
