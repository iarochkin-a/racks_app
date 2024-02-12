from typing import List

from pydantic import BaseModel
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.settings import Database_utils

async_url = Database_utils().get_async_url()
async_engine = create_async_engine(async_url, echo=False)

Session = async_sessionmaker(bind=async_engine)


class BaseSQLRepository:
    model = None
    schema: BaseModel = None

    def __init__(self, session):
        self.session: AsyncSession = session

    async def set_obj(self, data) :
        query = insert(self.model).values(**data)
        await self.session.execute(query)
        await self.session.commit()

    async def get_obj(self, obj_id: int) -> BaseModel:
        query = (select(self.model)
                 .where(self.model.id == obj_id)
                 )
        obj_row = await self.session.execute(query)
        if not obj_row:
            raise Exception(f'{self.model.__name__} with id {self.model.id} not found.')
        obj_model = obj_row.scalar_one()
        return self.schema.model_validate(obj_model)

    async def get_all_obj(self) -> list[BaseModel]:
        query = select(self.model)
        obj_row = await self.session.execute(query)
        obj_scalars = obj_row.scalars().all()
        obj_schemas = [self.schema.model_validate(row) for row in obj_scalars]
        return obj_schemas

    async def update_obj(self, obj_id: int, new_obj):
        query = update(self.model).values(new_obj).where(self.model.id == obj_id)
        await self.session.execute(query)
        await self.session.commit()

    async def delete_obj(self, obj_id: int):
        query = delete(self.model).where(self.model.id == obj_id)
        await self.session.execute(query)
        await self.session.commit()


class Base(DeclarativeBase):
    pass
