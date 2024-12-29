import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/transactions_db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    API_KEY: str = os.getenv("API_KEY", "your_secret_api_key")

settings = Settings()