#!/usr/bin/python3
"""Starts a Flask web app """
from models import storage
from models.state import State
from models.city import City
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display an HTML page with list of states with there cities
    sorted by state name """
    cities = storage.all(City).values()
    states = storage.all(State).values()
    s_states = sorted(states, key=lambda state: state.name)
    return render_template("8-cities_by_states.html",
                           states=s_states, cities=cities)


@app.teardown_appcontext
def tear_down(exc):
    """Remove the current SQLAlchemy session. """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
