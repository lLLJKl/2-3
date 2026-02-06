from fastapi import FastAPI
from kafka import KafkaProducer
from settings import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Producer"}