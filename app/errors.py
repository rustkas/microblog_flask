"""Error handlers for the Flask application."""
from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(_error):
    """Handle 404 Not Found errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(_error):
    """Handle 500 Internal Server errors."""
    db.session.rollback()
    return render_template('500.html'), 500
