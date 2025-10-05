# Task 10 - Flask + HTML Integration (Exercise File)
#
# 🧩 CHALLENGE: Modify the Flask app
#
# Requirements:
# - Add your name to the HTML template
# - Add a simple button function
# - Create a second route /about with custom content
# - Keep it simple - only 2 functions max in Flask
#
# 💡 TIP: You can use an AI assistant to help you with this task!
# Ask questions like:
# - "How do I add my name to a Flask template?"
# - "How do I create a new route in Flask?"
# - "How do I add a button that does something in HTML?"
#
# Your code goes here:
# TODO: Modify the Flask app below this line

from flask import Flask, render_template, request

app = Flask(__name__)

# TODO: Add your functions here (max 2 functions)


@app.route("/")
def home():
    # TODO: Add your name to the template
    return render_template(
        "index.html", title="AI Flask App", message="Hello, Template!"
    )


# TODO: Add a second route /about with custom content
# @app.route('/about')
# def about():
#     return render_template('index.html', title="About Page", message="This is the about page!")

if __name__ == "__main__":
    app.run(debug=True)
