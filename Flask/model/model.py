import pandas as pd
from flaml import AutoML
from flaml.automl.ml import sklearn_metric_loss_score
import dabl
import pickle
from sklearn.model_selection import train_test_split

import time as tl

def timeStrToTimestamp(s):
    date, time = s.split("T")[0], ":".join(s.split("T")[1].split(":")[:-1])
    timestamp = date + " " + time
    timestamp = tl.mktime(tl.strptime(timestamp, '%Y-%m-%d %H:%M'))
    return timestamp

dataset = pd.read_pickle("earthquake.pkl")
dataset = dabl.clean(dataset)
dataset = dataset.dropna()

X = dataset[["time", "latitude", "longitude"]]
X["time"] = X["time"].map(timeStrToTimestamp)
y = dataset["mag"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
idx_train, idx_test = train_test_split(X.index, test_size=0.2, stratify=y, random_state=42)
X_train, X_test, y_train, y_test = X.loc[idx_train, :], X.loc[idx_test, :], y.loc[idx_train], y.loc[idx_test]

autoML = AutoML()

settings = {
    "time_budget": 240,  # total running time in seconds
    "metric": 'r2',  # primary metrics for regression can be chosen from: ['mae','mse','r2','rmse','mape']
    "estimator_list": ['lgbm'],  # list of ML learners; we tune lightgbm in this example
    "task": 'regression',  # task type    
    "log_file_name": 'earthquake_experiment.log',  # flaml log file
    "seed": 7654321,    # random seed
}

autoML.fit(X_train=X_train, y_train=y_train, **settings)
y_pred = autoML.predict(X_test)
print('r2', '=', 1 - sklearn_metric_loss_score('r2', y_pred, y_test))
print('mse', '=', sklearn_metric_loss_score('mse', y_pred, y_test))
print('mae', '=', sklearn_metric_loss_score('mae', y_pred, y_test))

pickle.dump(autoML, open("model.pkl", "wb"), pickle.HIGHEST_PROTOCOL)
