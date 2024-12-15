from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle

iris = load_iris()

X = iris.data
y = iris.target

clf = LogisticRegression(random_state=0, max_iter=1000).fit(X, y)

with open('server/model.pkl', 'wb') as file:
    pickle.dump(clf, file)

