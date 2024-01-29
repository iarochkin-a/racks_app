from src.service import RacksRepositoryInterface
from src.repository.schemas.racks import OutputRacksSchema, InputRacksSchema, OccupiedRacksSchema, MaxRackSizeInRoom


class RacksService:

    def __init__(self, RacksRepository: RacksRepositoryInterface):
        self.racks_repository = racks_repository

    async def set_obj_schema(self, data) -> int:
        await self.racks_repository.set_obj(data)

    async def get_obj_schema(self, obj_id: int) -> OutputRacksSchema:
        racks_schema: OutputRacksSchema = await self.racks_repository.get_obj(obj_id)
        return racks_schema

    async def get_all_obj_schema(self) -> list[OccupiedRacksSchema]:
        racks_schemas_list: [OutputRacksSchema] = await self.racks_repository.get_all_obj()
        return racks_schemas_list

    async def update_obj_schema(self, obj_id: int, rack_schema: InputRacksSchema) -> int:
        await self.racks_repository.update_obj(obj_id, rack_schema)

    async def delete_obj_schema(self, obj_id: int) -> int:
        await self.racks_repository.delete_obj(obj_id)

    async def get_occupied_racks(self) -> list[OccupiedRacksSchema]:
        occupied_rack_schema: OccupiedRacksSchema = await self.racks_repository.get_occupied_racks()
        return occupied_rack_schema

    async def get_rack_with_max_size(self) -> list[MaxRackSizeInRoom]:
        rack_with_max_size_schema: MaxRackSizeInRoom = await self.racks_repository.get_rack_with_max_size()
        return rack_with_max_size_schema
