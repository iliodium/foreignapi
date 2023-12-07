import random
import uvicorn

from fastapi import FastAPI, File, UploadFile, Request

app = FastAPI(
    title="service"
)


@app.post("/yolo")
async def yolo(request: Request):
    data: bytes = await request.body()
    return {"status": 200}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
