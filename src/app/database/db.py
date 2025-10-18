import asyncio
import os
from dotenv import load_dotenv

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.app.models.users_models import User
from src.app.models.orders_models import Order

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "db-order-fastapi"

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    database = client["db-order-fastapi"]

    # Inicializa Beanie com os modelos
    await init_beanie(database=database, document_models=[User, Order])
