"""Routes for the Flask application."""

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Render the login page."""
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}"
        )
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)
