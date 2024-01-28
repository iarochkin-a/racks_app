from src.service import CustomersRepositoryInterface
from src.repository.schemas.customers import InputCustomersSchema, OutputCustomersSchema


class CustomersService:

    def __init__(self, customersRepository: CustomersRepositoryInterface):
        self._customersRepository = customersRepository

    async def set_obj_schema(self, data) -> int:
        new_customer_id: OutputCustomersSchema = await self._customersRepository.set_obj(data)
        return new_customer_id

    async def get_obj_schema(self, obj_id: int) -> OutputCustomersSchema:
        customer_schema: OutputCustomersSchema = await self._customersRepository.get_obj(obj_id)
        return customer_schema

    async def get_all_obj_schema(self) -> list[OutputCustomersSchema]:
        customers_schemas_list: [OutputCustomersSchema] = await self._customersRepository.get_all_obj()
        return customers_schemas_list

    async def update_obj_schema(self, obj_id: int, rack_schema: InputCustomersSchema) -> int:
        updated_customer_id: OutputCustomersSchema = await self._customersRepository.update_obj(obj_id, rack_schema)
        return updated_customer_id

    async def delete_obj_schema(self, obj_id: int) -> int:
        deleted_customer_id: OutputCustomersSchema = await self._customersRepository.delete_obj(obj_id)
        return deleted_customer_id
