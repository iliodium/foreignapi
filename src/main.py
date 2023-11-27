import os
import sys

from fastapi import FastAPI
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from order.router import router as orders_router

app = FastAPI(
    title="Cafeteria"
)

app.include_router(orders_router)

