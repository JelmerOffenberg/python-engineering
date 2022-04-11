from sklearn.ensemble import RandomForestClassifier
from data.load_data import load_iris_data
from utils import save_model


def train(model, X, y):
    # Return a fitted model on the given data.
    return model.fit(X, y)


def train_model(name='random_forest_v1.joblib'):
    """Wrapper function, handles model training and storing."""

    # Model choice (could be something in a config)
    model = RandomForestClassifier()

    # Load data
    X, y = load_iris_data()

    # Train model
    trained_model = train(model, X, y)

    # Save model
    save_model(trained_model, name)


if __name__ == '__main__':
    train_model()