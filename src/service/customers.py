from src.service import CustomersRepositoryInterface
from src.repository.schemas.customers import InputCustomersSchema, OutputCustomersSchema


class CustomersService:

    def __init__(self, CustomersRepository: CustomersRepositoryInterface):
        self.CustomersRepository = CustomersRepository

    async def set_obj_schema(self, data) -> int:
        await self.CustomersRepository.set_obj(data)

    async def get_obj_schema(self, obj_id: int) -> OutputCustomersSchema:
        customer_schema: OutputCustomersSchema = await self.CustomersRepository.get_obj(obj_id)
        return customer_schema

    async def get_all_obj_schema(self) -> list[OutputCustomersSchema]:
        customers_schemas_list: [OutputCustomersSchema] = await self.CustomersRepository.get_all_obj()
        return customers_schemas_list

    async def update_obj_schema(self, obj_id: int, rack_schema: InputCustomersSchema) -> int:
        await self.CustomersRepository.update_obj(obj_id, rack_schema)

    async def delete_obj_schema(self, obj_id: int) -> int:
        await self.CustomersRepository.delete_obj(obj_id)

