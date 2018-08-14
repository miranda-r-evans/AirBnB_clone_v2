#!/usr/bin/python3
'''
starts a Flask web app
'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''
        testing basic flask app
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
        testing basic flask app with /hbnb path
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
        route with variable
    '''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text='is cool'):
    '''
        route with optional variable
    '''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    '''
        route testing if input is an int
    '''
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
