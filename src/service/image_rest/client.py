import asyncio

import aiohttp
import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Trading App"
)

URL = "http://158.220.112.237:3005/"
# URL = "http://127.0.0.1:8001/"

count = 100


async def main():
    imageFilename = r"IMG_0898.jpeg"
    imageFilename = r"IMG_0898 2.jpeg"
    imageFilename = r"IMG_0898 3.jpeg"
    imageFilename = r"IMG_0898 4.jpeg"

    imageFileObj = open(imageFilename, "rb")
    imageBinaryBytes = imageFileObj.read()
    import time
    t1 = time.time()
    for _ in range(count):
        async with aiohttp.ClientSession() as session:
            await session.post(URL, data=imageBinaryBytes)

    t2 = time.time()

    time = t2 - t1
    size = 4914
    volume = size * count
    print(f'count={count}')
    print(f'size={size}KB')
    print(f'time={time}')
    print(f'volume={volume}')
    print(f'speed={volume / time}KB')
    print(f'speed={volume / time / 1024}MB')
    print(f'speed={volume / time / 1024 / 1024}GB')

    return "OK"


@app.post("/")
async def get_yolo():
    imageFilename = r"IMG_0898.jpeg"

    imageFileObj = open(imageFilename, "rb")
    imageBinaryBytes = imageFileObj.read()
    import time
    t1 = time.time()
    for _ in range(count):
        async with aiohttp.ClientSession() as session:
            await session.post(URL, data=imageBinaryBytes)

    t2 = time.time()

    time = t2 - t1
    size = 4914
    volume = size * count
    print(f'count={count}')
    print(f'size={size}KB')
    print(f'time={time}')
    print(f'volume={volume}')
    print(f'speed={volume / time}KB')
    print(f'speed={volume / time / 1024}MB')
    print(f'speed={volume / time / 1024 / 1024}GB')

    return "OK"


if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8012)
    uvicorn.run(app, host="127.0.0.1", port=3000)
    # asyncio.run(main())
