from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI with MongoDB"
    MONGO_URI: str = Field(..., env="MONGO_URI")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"

settings = Settings()
