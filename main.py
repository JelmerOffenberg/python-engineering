from fastapi import FastAPI
from model.utils import setup_logger

logger = setup_logger()
app = FastAPI()

@app.get("/hello")
def hello():
    logger.info("Received request.")
    return {"answer": "goodbye"}
