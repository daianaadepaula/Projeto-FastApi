from fastapi import FastAPI
from src.app.database.db import init_db

from src.app.routes.auth_routes import auth_router
from src.app.routes.order_routes import order_router

app = FastAPI(title="FastAPI + MongoDB")

app.include_router(auth_router)
app.include_router(order_router)

@app.on_event("startup")
async def startup_event():
    await init_db()
