#!/usr/bin/python3
"""
script that starts a fask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<path:text>', strict_slashes=False, defaults={
    'text': 'is cool'})
@app.route('/c/', strict_slashes=False)
def c_route(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<path:text>', strict_slashes=False, defaults={
    'text': 'is cool'})
@app.route('/python/', strict_slashes=False)
def python_route(text):
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
