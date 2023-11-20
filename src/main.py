from fastapi import FastAPI, Query
from typing import List

from orders.router import router as orders_router

app = FastAPI(
    title="Cafeteria"
)

app.include_router(orders_router)

