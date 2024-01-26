from src.service import CustomersRepositoryInterface
from src.repository.schemas.customers import InputCustomersSchema, OutputCustomersSchema


class CustomersService:

    def __init__(self, customersRepository: CustomersRepositoryInterface):
        self._customersRepository = customersRepository

    async def set_obj_schema(self, data):
        obj_schema: OutputCustomersSchema = await self._customersRepository.set_obj(data)
        return obj_schema

    async def get_obj_schema(self, obj_id: int) -> OutputCustomersSchema:
        obj_schema: OutputCustomersSchema = await self._customersRepository.get_obj(obj_id)
        return obj_schema

    async def get_all_obj_schema(self):
        obj_schema_list: [OutputCustomersSchema] = await self._customersRepository.get_all_obj()
        return obj_schema_list

    async def update_obj_schema(self, obj_id: int, rack_schema: InputCustomersSchema):
        obj_schema: OutputCustomersSchema = await self._customersRepository.update_obj(obj_id, rack_schema)
        return obj_schema

    async def delete_obj_schema(self, obj_id: int):
        obj_schema: OutputCustomersSchema = await self._customersRepository.delete_obj(obj_id)
        return obj_schema
