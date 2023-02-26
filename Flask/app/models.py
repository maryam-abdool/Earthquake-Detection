import numpy as np
from pickle5 import load
import pickle5 as pickle


class Model:
    def __init__(self, path="app/saved_models/model.pkl"):
        self.model = load(open(path, "rb")).model.estimator

    def predict(self, inputs):
        final_features = [np.array(inputs)]
        prediction = self.model.predict(final_features)
        output = prediction[0]
        return output
    
model = Model("app/saved_models/model.pkl")