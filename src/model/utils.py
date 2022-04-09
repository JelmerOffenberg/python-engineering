from pathlib import Path
from joblib import dump, load


def save_model(model, name):
    path = Path(__file__).parent.parent.parent / "models" / name
    dump(model, path)


def load_model(name):
    path = Path(__file__).parent.parent.parent / "models" / name
    return load(path)
