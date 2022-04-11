from model.predict import predict


def test_predict():
    MODEL_NAME = 'local'
    FEATURE_VECTOR = [[1, 1, 1, 1]]

    result = predict(MODEL_NAME, FEATURE_VECTOR)

    # Classification model returns sigmoid (value between 0, 1)
    assert 0 <= result <= 1