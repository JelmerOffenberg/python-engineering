import sys
import logging

from pathlib import Path
from joblib import dump, load

def save_model(model, name):
    path = Path(__file__).parent.parent.parent / "models" / name
    dump(model, path)


def load_model(name)
    path = Path(__file__).parent.parent.parent / "models" / name
    return load(path)


def setup_logger():
    """Set up some basic stream logging."""
    log_format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(
        stream = sys.stdout,
        format = log_format,
        level = logging.INFO
    )

    logger = logging.getLogger()

    return logger
