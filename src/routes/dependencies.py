from src.repository.sql_repositopy.racks import RacksRepository
from src.repository.sql_repositopy.rooms import RoomsRepository
from src.repository.sql_repositopy.customers import CustomersRepository
from src.repository.sql_repositopy import Session
from src.tools.cookie import CookieTools
from src.repository.schemas.auth import UserTokenSchema
from fastapi import Request, HTTPException
import requests


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


async def auth_middleware(request: Request):
    user_token_schema: UserTokenSchema = await CookieTools.get_tokens_from_cookie(request)
    print(user_token_schema)
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = requests.post(f'http://auth_app:5050/token/verify_tokens', headers=headers,
                              data=user_token_schema.model_dump_json(indent=2))
    print(response.json())
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail='User didnt auth'
        )
    else:
        return {
            'response': response.status_code,
            'data': response.json()
        }