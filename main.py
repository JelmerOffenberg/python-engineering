from fastapi import FastAPI
from model.utils import load_model, setup_logger
from api.requests import PredictRequest, PredictRequestEx6

logger = setup_logger()
app = FastAPI()

# Global initialisation
model = load_model(name='local')

simple_cache = []

@app.get("/hello")
def hello():
    return {"answer": "goodbye"}


@app.post("/predict")
def predict(data: PredictRequest):
    # Transform incoming request data class into a vector
    vector = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # Call global model predict on the request vector
    predict = model.predict(vector)[0]
    logger.info(f"Predict value is: {predict}")

    # Return result
    return {"result": f"{predict}"}


@app.post("/predict_ex6")
def predict(data: PredictRequestEx6):
    if data.test:
        logger.info(data)
        return {"result": 42}

    else:
        # Transform incoming request data class into a vector
        vector = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]]

        # Call global model predict on the request vector
        predict = model.predict(vector)[0]
        logger.info(f"Predict value is: {predict}")

        # Return result
        return {"result": f"{predict}"}


@app.post("/predict_ex7")
def predict(data: PredictRequest):
    # Transform incoming request data class into a vector
    vector = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # Only run this if there are cache variables
    if len(simple_cache) > 0:
        for cache_data, cache_result in simple_cache:
            if data == cache_data:
                logger.info("Cache hit")
                return {"result": f"{cache_result}"}

    # Call global model predict on the request vector
    predict = model.predict(vector)[0]
    logger.info(f"Predict value is: {predict}")

    # Caching result
    simple_cache.append((data, predict))

    # Return result
    return {"result": f"{predict}"}


@app.get("/cache")
def predict():
    return {"result": f"{simple_cache}"}
