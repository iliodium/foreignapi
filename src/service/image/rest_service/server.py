import pickle
import uvicorn

from fastapi import FastAPI, Request

# from config import host, port

app = FastAPI(
    title="service"
)


@app.get("/t")
async def send_check(data):
# async def send_check():
    # data: bytes = await request.body()
    # data: bytes = await request.body()
    print(data)

    #data = pickle.loads(data)
    return {"status": 200}
    # return {"status": data["name"]}


if __name__ == "__main__":
    # uvicorn.run(app, host=host, port=port)
    pass
