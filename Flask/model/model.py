import pandas as pd
from flaml import AutoML
from flaml.automl.ml import sklearn_metric_loss_score
import dabl
import pickle
from sklearn.model_selection import train_test_split

from datetime import datetime

def timeStrToTimestamp(s):
    date, time = s.split("T")[0], ":".join(s.split("T")[1].split(":")[:-1])
    timestamp = date + " " + time
    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    return timestamp


if __name__ == "__main__":
    dataset = pd.read_pickle("earthquake.pkl") # some problems with this file
    dataset = dataset[["time", "latitude", "longitude", "mag"]]
    dataset = dabl.clean(dataset)
    dataset = dataset.dropna()

    dataset["time"] = dataset["time"].map(timeStrToTimestamp)
    X = dataset.set_index("time")
    X = X.reset_index()

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    idx_train, idx_test = train_test_split(X.index, test_size=0.2, random_state=42)
    X_train, X_test = X.loc[idx_train, :], X.loc[idx_test, :]

    autoML = AutoML()

    settings = {
        "time_budget": 240,  # total running time in seconds
        "metric": 'mape',  # primary metrics for regression can be chosen from: ['mae','mse','r2','rmse','mape']
        "task": 'ts_forecast',  # task type
        "log_file_name": 'earthquake_experiment.log',  # flaml log file
        "eval_method": "holdout",
        "seed": 7654321,    # random seed
    }

    autoML.fit(dataframe=X_train, label="mag", period=10, **settings)
    y_pred = autoML.predict(X_test.drop(columns=["mag"]))
    print('mape', '=', sklearn_metric_loss_score('mape', y_pred, X_test.mag))

    pickle.dump(autoML, open("model.pkl", "wb"), pickle.HIGHEST_PROTOCOL)
