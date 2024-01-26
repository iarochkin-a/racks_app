from src.repository.sql_repositopy import BaseSQLRepository
from src.service import CustomersRepositoryInterface
from src.repository.sql_repositopy.models import CustomerORM
from src.repository.schemas.customers import OutputCustomersSchema


class CustomersRepository(BaseSQLRepository, CustomersRepositoryInterface):
    model = CustomerORM
    schema = OutputCustomersSchema