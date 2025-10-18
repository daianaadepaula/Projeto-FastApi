import asyncio
import os
from dotenv import load_dotenv

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.app.models.users_models import User
from src.app.models.orders_models import Order

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

# MONGO_URI = "mongodb+srv://db-order-fastapi:JpuzoP91CYE0T0BqQ5TMxH@cluster0.1s84h9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    database = client.get_default_database()  # usa o nome definido no URI

    # Inicializa Beanie com os modelos
    await init_beanie(database=database, document_models=[User, Order])
