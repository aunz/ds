#!/usr/bin/env python

import os
from flask import Flask, request, render_template, jsonify

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='public')

@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    

