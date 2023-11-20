from fastapi import FastAPI

from orders.router import router as orders_router

app = FastAPI(
    title="Cafeteria"
)

app.include_router(orders_router)

