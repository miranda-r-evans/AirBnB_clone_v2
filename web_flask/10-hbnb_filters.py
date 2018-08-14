#!/usr/bin/python3
'''
starts a Flask web app for HBNB
'''

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb():
    '''
        returns HBNB index page
    '''
    all_states = list(storage.all('State').values())
    all_cities = list(storage.all('City').values())
    states_cities = ({state:
                      [city for city in all_cities
                       if city.state_id == state.id]
                      for state in all_states})
    all_amenities = list(storage.all('Amenity').values())
    return render_template('10-hbnb_filters.html',
                           states_cities=states_cities, amenities=all_amenities)


@app.teardown_appcontext
def close_storage(error):
    '''
        closes out storage
    '''
    storage.close()

app.run(host='0.0.0.0', port=5000, debug=True)
