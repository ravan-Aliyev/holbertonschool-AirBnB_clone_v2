#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Display c {text}.
    /python/<text>: Display python {text}.
    /number/<n>: Display number.
"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_world():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def what_is_c(text):
    """Display C {text}"""
    return (f"C {escape(text.replace('_', ' '))}")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def what_is_python(text="is cool"):
    """Display python {text}"""
    return (f"Python {escape(text.replace('_', ' '))}")


@app.route("/number/<int:n>", strict_slashes=False)
def what_is_number(n: int):
    """Display number"""
    return (f"{escape(n)} is a number")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
