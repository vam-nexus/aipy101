"""
Concept: Flask Chatbot Integration

This example demonstrates integrating LLM chatbots into Flask web applications.
Students will learn about combining web frameworks with AI APIs for interactive experiences.
"""

# Task 13 - Flask Chatbot Integration (Example File)
# This file demonstrates Flask + LLM chatbot integration

from flask import Flask, render_template, request, redirect, session, jsonify
import json
import os

# suppress warnings
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore")

# import libraries
import requests

from together import Together
import textwrap

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)


## FUNCTION 1: This Allows Us to Prompt the AI MODEL
# -------------------------------------------------
def prompt_llm(prompt, with_linebreak=False):
    # This function allows us to prompt an LLM via the Together API

    # model
    model = "meta-llama/Meta-Llama-3-8B-Instruct-Lite"

    # Make the API call
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    output = response.choices[0].message.content

    if with_linebreak:
        # Wrap the output
        wrapped_output = textwrap.fill(output, width=50)

        return wrapped_output
    else:
        return output


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


# Load chat history from JSON file
def load_chat_history():
    if os.path.exists("chat_history.json"):
        with open("chat_history.json", "r") as f:
            return json.load(f)
    return {}


def save_chat_history(chat_history):
    with open("chat_history.json", "w") as f:
        json.dump(chat_history, f)


users = load_users()
todos = load_todos()
chat_history = load_chat_history()


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
    user_chat = chat_history.get(username, [])

    return render_template(
        "dashboard.html", username=username, todos=user_todos, chat_history=user_chat
    )


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


@app.route("/chat", methods=["POST"])
def chat():
    if "user" not in session:
        return jsonify({"error": "Not logged in"})

    username = session["user"]
    user_message = request.json.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"})

    # Create chatbot prompt
    user_todos = todos.get(username, [])
    todo_context = ""
    if user_todos:
        todo_list = "\n".join(
            [
                f"- {todo['task']} ({'✓' if todo['completed'] else '○'})"
                for todo in user_todos
            ]
        )
        todo_context = f"\n\nUser's current todo list:\n{todo_list}"

    prompt = f"""
    You are a helpful AI assistant for a todo list app. The user is asking: "{user_message}"
    
    Instructions:
    - Be friendly and helpful
    - Keep responses concise (max 2-3 sentences)
    - You can help with todo-related questions
    - If they ask about their tasks, refer to their todo list
    {todo_context}
    
    Respond to the user's message:
    """

    try:
        response = prompt_llm(prompt)

        # Save chat history
        if username not in chat_history:
            chat_history[username] = []

        chat_history[username].append({"user": user_message, "bot": response})

        # Keep only last 10 messages
        if len(chat_history[username]) > 10:
            chat_history[username] = chat_history[username][-10:]

        save_chat_history(chat_history)

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": "Sorry, I'm having trouble responding right now."})


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True, port=5013)
