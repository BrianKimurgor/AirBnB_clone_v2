#!/usr/bin/python3
"""
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
 return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
 return 'HBNB'

@app.route('/c/<path:text>', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/c/', strict_slashes=False)
def c_route(text):
 text = text.replace('_', ' ')
 return f'C {text}'

@app.route('/python/<path:text>', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/', strict_slashes=False)
def python_route(text):
 text = text.replace('_', ' ')
 return f'Python {text}'

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
 return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n=None):
 return render_template('5-number.html', n=n)

if __name__ == "__main__":
 app.run(host='0.0.0.0', port=5000)
