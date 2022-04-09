from fastapi import FastAPI
from model.utils import load_model
from api.requests import PredictRequest


app = FastAPI()

model = load_model(name='local')

@app.get("/hello")
def hello():
    return {"answer": "hello"}


@app.post("/predict")
async def predict(data: PredictRequest):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # Predict
    prediction = model.predict(X=features)[0]

    # Return the Result
    return { 'class' : prediction}
