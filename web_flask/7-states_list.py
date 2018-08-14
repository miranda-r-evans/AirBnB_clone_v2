#!/usr/bin/python3
'''
starts a Flask web app
'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    '''
        returns a list of states (html)
    '''
    all_states = list(storage.all('State').values())
    return render_template('7-states_list.html', all_states=all_states)


@app.teardown_appcontext
def close_storage(error):
    '''
        closes out storage
    '''
    storage.close()

app.run(host='0.0.0.0', port=5000, debug=True)
