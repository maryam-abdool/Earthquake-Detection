import numpy as np
import pickle5 as pickle


class Model:
    def __init__(self, path="model.pkl"):
        self.model = pickle.load(open(path, "rb")).model.estimator


    def predict(self, inputs):
        final_features = [np.array(inputs)]
        prediction = self.model.predict(final_features)
        output = prediction[0]
        return output