from src.service import RoomsRepositoryInterface
from src.repository.schemas.rooms import InputRoomsSchema, OutputRoomSchema, RoomsWithOccupiedRackSchema


class RoomsService:

    def __init__(self, RoomsRepository: RoomsRepositoryInterface):
        self.RoomsRepository = RoomsRepository

    async def set_obj_schema(self, data) -> int:
        await self.RoomsRepository.set_obj(data)

    async def get_obj_schema(self, obj_id: int) -> OutputRoomSchema:
        room_schema: OutputRoomSchema = await self.RoomsRepository.get_obj(obj_id)
        return room_schema

    async def get_all_obj_schema(self) -> list[OutputRoomSchema]:
        rooms_schemas_list: [OutputRoomSchema] = await self.RoomsRepository.get_all_obj()
        return rooms_schemas_list

    async def update_obj_schema(self, obj_id: int, rack_schema: InputRoomsSchema) -> int:
        await self.RoomsRepository.update_obj(obj_id, rack_schema)

    async def delete_obj_schema(self, obj_id: int) -> int:
        await self.RoomsRepository.delete_obj(obj_id)

    async def get_room_with_occupied_racks(self) -> list[RoomsWithOccupiedRackSchema]:
        obj_schema = await self.RoomsRepository.get_room_with_occupied_racks()
        return obj_schema
