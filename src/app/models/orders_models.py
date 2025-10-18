from beanie import Document, Indexed, Link
from pydantic import Field
from uuid import UUID, uuid4
from enum import Enum
from src.app.models.users_models import User

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"

class Order(Document):
    id: UUID = Field(default_factory=uuid4, primary_field=True)
    status: OrderStatus = Field(default=OrderStatus.PENDING)
    user: Link[User]
    price: float = Field(default=0.0)
    # items: List[...] se quiser depois

    class Settings:
        name = "orders"  # Nome da coleção no MongoDB

class OrderItem(Document):
    id: UUID = Field(default_factory=uuid4, primary_field=True)
    quantity: int
    flavor: str
    size: int
    unit_price: float
    order: Link[Order]

    class Settings:
        name = "order_items"  # Nome da coleção no MongoDB