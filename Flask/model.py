import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv("earthquake.csv")
X, y = dataset.iloc[:, :-1], dataset.iloc[:, -1]

classifier = DecisionTreeClassifier()
classifier.fit(X, y)

pickle.dump(classifier, open("model.pkl", "wb"))
