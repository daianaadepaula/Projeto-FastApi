from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.app.core.config import settings
from src.app.models.users_models import User
from src.app.models.orders_models import Order

DB_NAME = "db-order-fastapi"

async def init_db():
    client = AsyncIOMotorClient(settings.MONGO_URI)
    database = client[DB_NAME]

    # Inicializa Beanie com os modelos
    await init_beanie(
        database=database,
        document_models=[User, Order]
    )
