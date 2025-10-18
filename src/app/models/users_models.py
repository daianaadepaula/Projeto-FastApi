from beanie import Document, Indexed
from pydantic import Field
from uuid import UUID, uuid4

class User(Document):
    id: UUID = Field(default_factory=uuid4, primary_field=True)
    name: str
    email: Indexed(str, unique=True)
    password: str = Field(min_length=6)
    active: bool = Field(default=True)
    admin: bool = Field(default=False)

    class Settings:
        name = "users"  # Nome da coleção no MongoDB
