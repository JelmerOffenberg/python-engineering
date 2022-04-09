from model.utils import load_model


def predict(model_name, X):
    model = load_model(model_name)
    return model.predict(X)
