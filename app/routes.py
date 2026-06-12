"""Routes for the Flask application."""
from app import app


@app.route("/")
@app.route("/index")
def index():
    """Route for the home page."""
    return "Hello, World!"
