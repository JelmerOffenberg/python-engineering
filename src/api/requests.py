from pydantic import BaseModel


class PredictRequest(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float


class PredictRequestEx6(BaseModel):
    test: bool
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
