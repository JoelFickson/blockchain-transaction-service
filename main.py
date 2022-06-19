from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def serveRoot():
    return {"message": "Welcome to my blockchain service"}

@app.get('/transaction/{transaction_id}')
def findTransaction(transaction_id):
    return {"TransactionID": transaction_id}