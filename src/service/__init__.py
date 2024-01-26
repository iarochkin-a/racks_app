import abc
from pydantic import BaseModel


class RacksRepositoryInterface(abc.ABC):

    @abc.abstractmethod
    async def set_obj(self, obj_schema: BaseModel):
        ...

    @abc.abstractmethod
    async def get_obj(self, obj_id: int):
        ...

    @abc.abstractmethod
    async def get_all_obj(self):
        ...

    @abc.abstractmethod
    async def update_obj(self, obj_id: int, obj_schema: BaseModel):
        ...

    @abc.abstractmethod
    async def delete_obj(self, obj_id: int):
        ...

    @abc.abstractmethod
    async def get_occupied_racks(self):
        ...

    @abc.abstractmethod
    async def get_rack_with_max_size(self):
        ...


class RoomsRepositoryInterface(abc.ABC):

    @abc.abstractmethod
    async def set_obj(self, obj_schema: BaseModel):
        ...

    @abc.abstractmethod
    async def get_obj(self, obj_id: int):
        ...

    @abc.abstractmethod
    async def get_all_obj(self):
        ...

    @abc.abstractmethod
    async def update_obj(self, obj_id: int, obj_schema: BaseModel):
        ...

    @abc.abstractmethod
    async def delete_obj(self, obj_id: int):
        ...

    @abc.abstractmethod
    async def get_room_with_occupied_racks(self):
        ...


class CustomersRepositoryInterface(abc.ABC):

    @abc.abstractmethod
    async def set_obj(self, obj_schema: BaseModel):
        ...

    @abc.abstractmethod
    async def get_obj(self, obj_id: int):
        ...

    @abc.abstractmethod
    async def get_all_obj(self):
        ...

    @abc.abstractmethod
    async def update_obj(self, obj_id: int, obj_schema: BaseModel):
        ...

    @abc.abstractmethod
    async def delete_obj(self, obj_id: int):
        ...