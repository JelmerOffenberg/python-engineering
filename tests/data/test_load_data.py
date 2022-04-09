import numpy as np
from data.load_data import load_iris_data


def test_load_iris_data():
    X, y = load_iris_data()

    # Test non empty data
    assert len(X) > 1
    assert len(y) > 1

    # Test data type
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
