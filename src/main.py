import os
import sys

from fastapi import FastAPI
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from menu.router import router as menu_router
from order.router import router as order_router

app = FastAPI(
    title="Cafeteria"
)

app.include_router(menu_router)
app.include_router(order_router)
