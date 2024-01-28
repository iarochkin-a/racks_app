from src.service import RacksRepositoryInterface
from src.repository.schemas.racks import OutputRacksSchema, InputRacksSchema, OccupiedRacksSchema, MaxRackSizeInRoom


class RacksService:

    def __init__(self, racksRepository: RacksRepositoryInterface):
        self._racksRepository = racksRepository

    async def set_obj_schema(self, data) -> int:
        new_racks_id: OutputRacksSchema = await self._racksRepository.set_obj(data)
        return new_racks_id

    async def get_obj_schema(self, obj_id: int) -> OutputRacksSchema:
        racks_schema: OutputRacksSchema = await self._racksRepository.get_obj(obj_id)
        return racks_schema

    async def get_all_obj_schema(self) -> list[OccupiedRacksSchema]:
        racks_schemas_list: [OutputRacksSchema] = await self._racksRepository.get_all_obj()
        return racks_schemas_list

    async def update_obj_schema(self, obj_id: int, rack_schema: InputRacksSchema)-> int:
        updated_racks_id: OutputRacksSchema = await self._racksRepository.update_obj(obj_id, rack_schema)
        return updated_racks_id

    async def delete_obj_schema(self, obj_id: int)-> int:
        deleted_racks_id: OutputRacksSchema = await self._racksRepository.delete_obj(obj_id)
        return deleted_racks_id

    async def get_occupied_racks(self) -> list[OccupiedRacksSchema]:
        occupied_rack_schema: OccupiedRacksSchema = await self._racksRepository.get_occupied_racks()
        return occupied_rack_schema

    async def get_rack_with_max_size(self) -> list[MaxRackSizeInRoom]:
        rack_with_max_size_schema: MaxRackSizeInRoom = await self._racksRepository.get_rack_with_max_size()
        return rack_with_max_size_schema


