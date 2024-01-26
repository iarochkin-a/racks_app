from src.service import RoomsRepositoryInterface
from src.repository.schemas.rooms import InputRoomsSchema, OutputRoomsSchema


class RoomsService:

    def __init__(self, roomsRepository: RoomsRepositoryInterface):
        self._roomsRepository = roomsRepository

    async def set_obj_schema(self, data):
        obj_schema: OutputRoomsSchema = await self._roomsRepository.set_obj(data)
        return obj_schema

    async def get_obj_schema(self, obj_id: int) -> OutputRoomsSchema:
        obj_schema: OutputRoomsSchema = await self._roomsRepository.get_obj(obj_id)
        return obj_schema

    async def get_all_obj_schema(self):
        obj_schema_list: [OutputRoomsSchema] = await self._roomsRepository.get_all_obj()
        return obj_schema_list

    async def update_obj_schema(self, obj_id: int, rack_schema: InputRoomsSchema):
        obj_schema: OutputRoomsSchema = await self._roomsRepository.update_obj(obj_id, rack_schema)
        return obj_schema

    async def delete_obj_schema(self, obj_id: int):
        obj_schema: OutputRoomsSchema = await self._roomsRepository.delete_obj(obj_id)
        return obj_schema

    async def get_room_with_occupied_racks(self):
        obj_schema = await self._roomsRepository.get_room_with_occupied_racks()
        return obj_schema
