import logging

from sqlalchemy.orm import DeclarativeBase
from pydantic_settings import BaseSettings, SettingsConfigDict


class Base(DeclarativeBase):
    pass


class Database_settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_HOST: str
    PGPORT: str
    POSTGRES_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env")


class Database_utils:
    def __init__(self):
        self.settings = Database_settings()

    def get_async_url(self) -> str:
        return (f'postgresql+asyncpg://{self.settings.POSTGRES_USER}:{self.settings.POSTGRES_PASSWORD}'
                f'@{self.settings.POSTGRES_HOST}:{self.settings.PGPORT}/{self.settings.POSTGRES_DB}')
