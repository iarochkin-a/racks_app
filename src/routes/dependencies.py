from src.repository.sql_repositopy.racks import RacksRepository
from src.repository.sql_repositopy.rooms import RoomsRepository
from src.repository.sql_repositopy.customers import CustomersRepository
from src.repository.sql_repositopy import Session


async def get_racks_repository() -> RacksRepository:
    session = Session()
    yield RacksRepository(session)
    await session.close()


async def get_rooms_repository() -> RoomsRepository:
    session = Session()
    yield RoomsRepository(session)
    await session.close()


async def get_customers_repository() -> CustomersRepository:
    session = Session()
    yield CustomersRepository(session)
    await session.close()

