import pandas as pd
import pickle
from flaml import AutoML

dataset = pd.read_csv("earthquake.csv")
X, y = dataset.iloc[:, :-1], dataset.iloc[:, -1]

settings = {
    "time_budget": 240,  # total running time in seconds
    "metric": 'r2',  # primary metrics for regression can be chosen from: ['mae','mse','r2','rmse','mape']
    "estimator_list": ['lgbm'],  # list of ML learners; we tune lightgbm in this example
    "task": 'regression',  # task type    
    "log_file_name": 'houses_experiment.log',  # flaml log file
    "seed": 7654321,    # random seed
}

autoML = AutoML()

autoML.fit(X_train=X, y_train=y, **settings)

pickle.dump(autoML, open("model.pkl", "wb"), pickle.HIGHEST_PROTOCOL)
