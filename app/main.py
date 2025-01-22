from fastapi import FastAPI

from app.schema import SuccessResponse

app = FastAPI()


@app.get("/")
async def hello():
    return SuccessResponse(data="Hello, World!")
