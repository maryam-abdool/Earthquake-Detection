import numpy as np
try:
    import pickle5
except:
    import pickle


class Model:
    def __init__(self, path="model.pkl"):
        try:
            self.model = pickle5.load(open(path, "rb")).model.estimator
        except:
            self.model = pickle.load(open(path, "rb")).model.estimator


    def predict(self, inputs):
        final_features = [np.array(inputs)]
        prediction = self.model.predict(final_features)
        output = prediction[0]
        return output