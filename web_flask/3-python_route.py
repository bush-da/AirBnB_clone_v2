#!/usr/bin/python3
""" script that starts a Flask web application:

    web application listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable
        /python/<text>: display “Python ”, followed by the value of the text variable
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display text variable value after C """
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text="is cool"):
    """ Display Python 'text' or default Python is cool """
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
