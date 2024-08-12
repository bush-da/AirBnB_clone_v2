#!/usr/bin/python3
"""Starts Flask web application."""
from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=""):
    """Display an HTML page with a list of states
    or a specific state and its cities."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    if id and states:
        for state in sorted_states:
            if id == state.id:
                cities = [city for city in storage.all(City).values()
                          if city.state_id == state.id]
                return render_template('9-states.html', state=state,
                                       cities=cities)
        return render_template('9-states.html')  # No state found with that id
    return render_template('9-states.html', states=sorted_states)


@app.teardown_appcontext
def tear_down(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
