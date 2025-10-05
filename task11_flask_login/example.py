"""
Concept: Flask Login & History

This example demonstrates Flask sessions, user authentication, and data persistence.
Students will learn about login systems, session management, and JSON file storage.
"""

# Task 11 - Flask Login & History (Example File)
# This file demonstrates a simple login system

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
    return [{"name": "admin", "password": "password"}]  # Default admin user


def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)


def find_user(username):
    """Find user by username in the list"""
    for user in users:
        if user["name"] == username:
            return user
    return None


users = load_users()


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

    # Check for success message from signup
    success_message = request.args.get("message")
    if success_message == "signup_success":
        return render_template(
            "login.html", success="Account created successfully! Please login."
        )

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if find_user(username):
            return render_template("signup.html", error="Username already exists")

        # Save new user to JSON
        users.append({"name": username, "password": password})
        save_users(users)

        # Redirect to login page with success message
        return redirect("/login?message=signup_success")

    return render_template("signup.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return f"Hello, {session['user']}! This is your dashboard."


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True, port=5010)
