"""
Concept: Flask + HTML Integration

This example demonstrates Flask web framework with HTML templates.
Students will learn about web routes, template rendering, and dynamic content.
"""

# Task 10 - Flask + HTML Integration (Example File)
# This file demonstrates Flask with HTML templates

from flask import Flask, render_template, request

app = Flask(__name__)


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    """Find the next prime number after n"""
    p = n + 1
    while not is_prime(p):
        p += 1
    return p


@app.route("/")
def home():
    return render_template(
        "index.html", title="AI Flask App", message="Hello, Template!"
    )


@app.route("/about")
def about():
    return render_template(
        "index.html", title="About Page", message="This is the about page!"
    )


if __name__ == "__main__":
    app.run(debug=True)
