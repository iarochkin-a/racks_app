from fastapi import APIRouter, Depends, FastAPI

from src.service.customers import CustomersService
from src.repository.schemas.customers import InputCustomersSchema, OutputCustomersSchema
from src.routes.dependencies import get_customers_repository

customers_router = APIRouter(
    prefix='/customers'
)


@customers_router.get('/get_customer', response_model=OutputCustomersSchema)
async def get_customer(
        customer_id: int,
        customers_repository=Depends(get_customers_repository)):
    customer_schema = await CustomersService(customers_repository).get_obj_schema(customer_id)
    return customer_schema


@customers_router.get('/get_all_customer', response_model=list[OutputCustomersSchema])
async def get_all_customer(customers_repository=Depends(get_customers_repository)
                           ) -> list[OutputCustomersSchema]:
    customers_schemas = await CustomersService(customers_repository).get_all_obj_schema()
    return customers_schemas


@customers_router.post('/set_customer')
async def set_customer(customer_schema: InputCustomersSchema,
                       customers_repository=Depends(get_customers_repository)
                       ):
    await CustomersService(customers_repository).set_obj_schema(customer_schema.__dict__)


@customers_router.put('/update_customer')
async def update_customer(customer_id: int,
                          customer_schema: InputCustomersSchema,
                          customers_repository=Depends(get_customers_repository)
                          ):
    await (CustomersService(customers_repository).update_obj_schema(customer_id, customer_schema.__dict__))


@customers_router.delete('/delete_customer')
async def delete_customer(customer_id: InputCustomersSchema,
                          customers_repository=Depends(get_customers_repository)
                          ):
    await CustomersService(customers_repository).delete_obj_schema(customer_id)

