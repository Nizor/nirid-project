#importing libraries
from fastapi import FastAPI, File, UploadFile
import uvicorn

#instance
app = FastAPI()

@app.get("/ping") #test endpoint
async def ping():
    return "Hello"


@app.post("/predict")
async def predict(
    file:UploadFile = File(...)
):
    pass

if __name__ == "__main__":
    uvicorn.run(app,host='localhost', port=8000)