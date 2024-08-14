#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0, port 5000"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display a HTML page like 8-index.html"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    places = sorted(storage.all(Place).values(), key=lambda place: place.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    owner = dict()
    users = storage.all(User).values()
    for user in users:
        owner[user.id] = f"{user.first_name} {user.last_name}"
    return render_template("100-hbnb.html", states=states, places=places, amenities=amenities, owner=owner)


@app.teardown_appcontext
def tear_down(exc):
    """Remove current SQLAlchemy session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
