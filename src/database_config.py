import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv


class Base(DeclarativeBase):
    pass


class Database_utils:

    @classmethod
    def get_async_url(cls) -> str:
        load_dotenv()
        POSTGRES_DB = os.getenv('POSTGRES_DB')
        POSTGRES_USER = os.getenv('POSTGRES_USER')
        POSTGRES_HOST = os.getenv('POSTGRES_HOST')
        POSTGRES_PORT = os.getenv('POSTGRES_PORT')
        POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
        return f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

