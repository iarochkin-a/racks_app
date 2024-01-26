from src.service import RacksRepositoryInterface
from src.repository.schemas.racks import OutputRacksSchema, InputRacksSchema, OccupiedRacksSchema, MaxRackSizeInRoom


class RacksService:

    def __init__(self, racksRepository: RacksRepositoryInterface):
        self._racksRepository = racksRepository

    async def set_obj_schema(self, data):
        obj_schema: OutputRacksSchema = await self._racksRepository.set_obj(data)
        return obj_schema

    async def get_obj_schema(self, obj_id: int) -> OutputRacksSchema:
        obj_schema: OutputRacksSchema = await self._racksRepository.get_obj(obj_id)
        return obj_schema

    async def get_all_obj_schema(self):
        obj_schema_list: [OutputRacksSchema] = await self._racksRepository.get_all_obj()
        return obj_schema_list

    async def update_obj_schema(self, obj_id: int, rack_schema: InputRacksSchema):
        obj_schema: OutputRacksSchema = await self._racksRepository.update_obj(obj_id, rack_schema)
        return obj_schema

    async def delete_obj_schema(self, obj_id: int):
        obj_schema: OutputRacksSchema = await self._racksRepository.delete_obj(obj_id)
        return obj_schema

    async def get_occupied_racks(self):
        obj_schema: OccupiedRacksSchema = await self._racksRepository.get_occupied_racks()
        return obj_schema

    async def get_rack_with_max_size(self):
        obj_schema: MaxRackSizeInRoom = await self._racksRepository.get_rack_with_max_size()
        return obj_schema


