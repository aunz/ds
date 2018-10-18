#!/usr/bin/env python
from flask import Flask, request, render_template, jsonify
import numpy as np
from keras.models import load_model


# model
model = load_model('./model_60.h5')
model._make_predict_function() # https://github.com/keras-team/keras/issues/2397

max_len = 60
chars = ['\n',  ' ',  '!',  '"',  "'",  '(',  ')',  ',',  '-',  '.',  ':',  ';',  '?',  'A',  'B',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'J',  'K',  'L',  'M',  'N',  'O',  'P',  'Q',  'R',  'S',  'T',  'U',  'V',  'W',  'Y',  'Z',  'a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z']
char_indices = dict((char, chars.index(char)) for char in chars) 

def sample(preds, temperature = 0.5):
    ''' function to sample the next char given the model's prediction
    Because given the same input, the predicted output will always be the same.
    This function take an array of preds (sum to 1), and a temperature param, return a new array of preds, then randomly select 1 element
    At a low temp, the new array of preds has a distribution similar to the old array
    Conversely, at a high temp, the new array of preds will be quite different from the old array
    Based on the new distribution of pred probability, the numpy np.random.multinomial is used to randomly select 1 element
    '''
    preds = np.asarray(preds).astype('float64')
    preds = np.log1p(preds) / temperature
    preds = np.expm1(preds)
    preds = preds / np.sum(preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def predict(text_seed, n_char = 420, temperature = 0.5):
    # given the seed_text, predict up to the next n_char
    # generated_text = f'{text_seed:>max_len}'[:max_len] # pad string to the right and only take up to max_len
    generated_text = text_seed.rjust(max_len)[:max_len]
    for i in range(n_char):
        sampled = np.zeros((1, max_len, len(chars))) # one hot encodes the chars generated so far
        for t, char in enumerate(generated_text):
            if char in char_indices: sampled[0, t, char_indices[char]] = 1.
        preds = model.predict(sampled, verbose=0)[0] # sample the next char
        next_index = sample(preds, temperature)
        next_char = chars[next_index]
        generated_text += next_char
        generated_text = generated_text[1:]
        text_seed += next_char
    return text_seed


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
