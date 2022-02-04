#importing libraries
from fastapi import FastAPI, File, UploadFile

#instance
app = FastAPI()

@app.get("/ping") #endpoint
async def ping():
    return "Hello"

@app.post("/predict") #endpoint
async def predict(
    file: UploadFile = File(...)
):
    pass