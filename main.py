from fastapi import FastAPI
from model.utils import setup_logger
from pydantic import BaseModel
from typing import Union
from time import sleep

logger = setup_logger()
app = FastAPI(docs_url="/", redoc_url=None)


class PostName(BaseModel):
    name: str
    value: Union[str, int]


class DataStore:
    def __init__(self):
        self.database = {}

    def add_data(self, key: str, value: str):
        self.database[key] = value
        return self.database

    def get_data(self, key):
        logger.info("Database hit")
        sleep(5)
        return self.database[key]

    def delete_data(self, key):
        del self.database[key]
        return self.database


class Cache:
    def __init__(self):
        self.database = {}

    def key_exists(self, key: str) -> bool:
        return key in self.database.keys()

    def add_data(self, key: str, value: str):
        self.database[key] = value
        return self.database

    def get_data(self, key):
        logger.info("Cache hit")
        return self.database[key]

    def delete_data(self, key):
        del self.database[key]
        return self.database


data_store = DataStore()
cache = Cache()


@app.get("/name")
def get_name(name: str):
    if cache.key_exists(name):
        return cache.get_data(name)
    else:
        value = data_store.get_data(name)
        cache.add_data(key=name, value=value)

        return value


@app.post("/name")
def post_name(input_: PostName):
    return data_store.add_data(key=input_.name, value=input_.value)


@app.delete("/name")
def delete_name(key: str):
    return data_store.delete_data(key)
