#!/usr/bin/python3
"""Script that starts a Flask web app."""


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


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Route handler for the /hbnb path.

    Returns:
        str: A message displaying "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_C_with_text(text):
    """
    Route handler for the /c/<text> path.

    Args:
        text (str): The text variable captured from the URL.

    Returns:
        str: A message displaying "C " followed by the value of the text
    variable.
    """
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text='is cool'):
    """
    Route handler for the /python/<text> path.

    Args:
        text (str): The text variable captured from the URL.

    Returns:
        str: A message displaying "Python " followed by the value of the
    text variable.
    """
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Route handler for the /number/<n> path.

    Args:
        n (int): The number variable captured from the URL.

    Returns:
        str: A message displaying "n is a number" only if n is an integer.
    """
    return f'{n} is a number'


if __name__ == '__main__':
    """
    Main entry point for the application.

    Starts the Flask web application on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
