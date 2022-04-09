from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from utils import save_model


def load_data():
    data = load_iris()
    return data.data, data.target


def train(model: LogisticRegression, X, y):
    reg = model.fit(X, y)

    return reg


def train_model(name='local'):
    # Load data
    X, y = load_data()

    # Train model
    model = train(LogisticRegression(), X, y)

    # Save model
    save_model(model, name)


if __name__ == '__main__':
    train_model()