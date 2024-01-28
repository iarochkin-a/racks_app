from src.service import RoomsRepositoryInterface
from src.repository.schemas.rooms import InputRoomsSchema, OutputRoomsSchema, RoomsWithOccupiedRackSchema


class RoomsService:

    def __init__(self, roomsRepository: RoomsRepositoryInterface):
        self._roomsRepository = roomsRepository

    async def set_obj_schema(self, data) -> int:
        new_room_id: OutputRoomsSchema = await self._roomsRepository.set_obj(data)
        return new_room_id

    async def get_obj_schema(self, obj_id: int) -> OutputRoomsSchema:
        room_schema: OutputRoomsSchema = await self._roomsRepository.get_obj(obj_id)
        return room_schema

    async def get_all_obj_schema(self) -> list[OutputRoomsSchema]:
        rooms_schemas_list: [OutputRoomsSchema] = await self._roomsRepository.get_all_obj()
        return rooms_schemas_list

    async def update_obj_schema(self, obj_id: int, rack_schema: InputRoomsSchema) -> int:
        updated_rooms_id: OutputRoomsSchema = await self._roomsRepository.update_obj(obj_id, rack_schema)
        return updated_rooms_id

    async def delete_obj_schema(self, obj_id: int) -> int:
        deleted_rooms_id: OutputRoomsSchema = await self._roomsRepository.delete_obj(obj_id)
        return deleted_rooms_id

    async def get_room_with_occupied_racks(self) -> list[RoomsWithOccupiedRackSchema]:
        obj_schema = await self._roomsRepository.get_room_with_occupied_racks()
        return obj_schema
