#!/usr/bin/python3
"""
Flask Web Application Package

This package defines a simple Flask web application with routes.

Usage:
1. Import the 'app' instance to run the Flask application.
2. Routes are defined in this file.
"""

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define routes
@app.route('/')
def hello_hbnb():
    """
    Route handler for the root path.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def display_hbnb():
    """
    Route handler for the /hbnb path.

    Returns:
        str: A message displaying "HBNB".
    """
    return 'HBNB'
