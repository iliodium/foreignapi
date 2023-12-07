import os
import sys

from fastapi import FastAPI

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from menu.router import router as orders_router
from registration.router import router as registration_order



app = FastAPI(
    title="Cafeteria"
)

app.include_router(orders_router)
app.include_router(registration_order)
# app.include_router(user__router)
