from sklearn.datasets import load_iris


# This file needs a function to load
def load_iris_data():
    X, y = load_iris(return_X_y=True)

    return X, y