# Task 11 - Flask Login & History (Exercise File)
#
# 🧩 CHALLENGE: Add signup functionality with JSON storage
#
# Requirements:
# - Add a signup route that saves user credentials to JSON file
# - Create a signup form in HTML
# - When user signs up, just say "Welcome [username]"
# - Keep it very simple - just save to JSON and show welcome message
#
# 💡 TIP: You can use an AI assistant to help you with this task!
# Ask questions like:
# - "How do I save data to a JSON file in Python?"
# - "How do I create a signup form in Flask?"
# - "How do I add a new route for user registration?"
#
# Your code goes here:
# TODO: Add signup functionality below this line

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
    return {}


def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)


users = load_users()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users.get(username) == password:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return f"Hello, {session['user']}! This is your dashboard."


# TODO: Add signup route here
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     # Your signup implementation here
#     pass


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
