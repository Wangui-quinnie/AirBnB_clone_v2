from flask import Flask
""" Script that starts a Flask web app displaying Hello HBNB and HBNB."""


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


if __name__ == '__main__':
    """
    Main entry point for the application.

    Starts the Flask web application on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
