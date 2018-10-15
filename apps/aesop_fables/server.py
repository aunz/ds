#!/usr/bin/env python
import os
from flask import Flask, request, render_template, jsonify

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='public')

@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')

@app.route('/predict', methods=['post'])
def route_predict():
  text_seed = request.get_json(force=True)
  print('Received:', text_seed['text_seed'])
  if 'text_seed' not in text_seed: return ''
  predicted_text = predict(text_seed['text_seed'])
  print('Prediction done', predicted_text)
  return predicted_text

if __name__ == '__main__':
    app.run(debug=True)
    

