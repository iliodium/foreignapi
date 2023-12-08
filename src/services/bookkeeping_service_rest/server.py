import os
import pickle
import sys

import uvicorn

from fastapi import FastAPI, Request

sys.path.insert(1, os.path.join(sys.path[0], '..\\..\\..'))

from src.services.config import HOST, PORT
from src.services.utils import calculate_tax

app = FastAPI(
    title="BookkeepingService",
)


@app.get("/BookkeepingService/v1")
async def calculate_tax_from_check(request: Request) -> int:
    data: dict = pickle.loads(await request.body())
    tax = calculate_tax(data.values())
    return tax


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT + 1)
