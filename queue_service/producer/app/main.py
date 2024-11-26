from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis_client import redis_client

app = FastAPI()

# Define a schema for data validation
class Data(BaseModel):
    name: str
    value: int

@app.post("/enqueue/")
def enqueue(data: Data):
    if data.value < 0:
        raise HTTPException(status_code=400, detail="Value must be non-negative.")
    
    redis_client.rpush("data_queue", data.json())
    return {"message": "Data enqueued successfully."}
