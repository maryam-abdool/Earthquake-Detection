from app import app
from flask import render_template
from flask import request, jsonify

import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))


@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text='Probability of earthquake $ {}'.format(output))


@app.route('/results', methods=['POST'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
