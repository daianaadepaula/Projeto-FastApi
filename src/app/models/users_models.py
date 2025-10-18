from beanie import Document
from pydantic import BaseModel
from pydantic import Field
from uuid import UUID, uuid4

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4, primary_field=True)
    name: str
    email: str = Field(unique=True)
    password: str
    active: bool = Field(default=True)
    admin: bool = Field(default=False)

    class Settings:
        name = "users"  # Nome da coleção no MongoDB
