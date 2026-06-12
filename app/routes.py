"""Routes for the Flask application."""

from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    """Render the home page."""
    user = {"username": "Miguel"}

    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
    # return render_template("index.html",  user=user)
    # return render_template("index.html", title="Home", user=user)
