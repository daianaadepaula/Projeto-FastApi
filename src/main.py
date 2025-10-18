from fastapi import FastAPI
from src.app.database.db import init_db
import asyncio

from src.app.routes.auth_routes import auth_router
from src.app.routes.order_routes import order_router

app = FastAPI(title="FastAPI + MongoDB")

app.include_router(auth_router)
app.include_router(order_router)

async def startup_event():
    await init_db()