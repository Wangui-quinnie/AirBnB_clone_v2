#!/usr/bin/python3
""" Script that starts a Flask web application."""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root path.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """
    Main entry point for the application.

    Starts the Flask web application on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
