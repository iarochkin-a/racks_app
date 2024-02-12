import json

from fastapi import APIRouter, Depends, Request, Response, FastAPI
import requests

from src.tools.cookie import CookieTools
from src.repository.schemas.auth import RegisterUserSchema, SingInUserSchema, UserTokenSchema

auth_router = APIRouter()


@auth_router.post('/register')
async def register_new_user(register_user_schema: RegisterUserSchema,
                            response: Response):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response_data = requests.post(f'http://auth_app:5050/auth/register', headers=headers,
                                  data=register_user_schema.model_dump_json(indent=2))
    print(response_data.json())
    await CookieTools.set_tokens_to_cookie(UserTokenSchema(**response_data.json()), response)
    return {
        'response': response_data.status_code,
        'data': response_data.json()
    }


@auth_router.post('/sing_in')
async def authorize_user(sing_in_user_schema: SingInUserSchema,
                         response: Response):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response_data = requests.post(f'http://auth_app:5050/auth/sing_in', headers=headers,
                                  data=sing_in_user_schema.model_dump_json(indent=2))
    await CookieTools.set_tokens_to_cookie(UserTokenSchema(**response_data.json()), response)
    return {
        'response': response.status_code,
        'data': response_data.json()
    }


@auth_router.post('/verify_tokens')
async def verify_tokens(request: Request,
                        response: Response):
    user_token_schema: UserTokenSchema = await CookieTools.get_tokens_from_cookie(request)
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response_data = requests.post(f'http://auth_app:5050/token/verify_tokens', headers=headers,
                                  data=user_token_schema.model_dump_json(indent=2))
    if response_data.status_code == 200:
        await CookieTools.set_tokens_to_cookie(UserTokenSchema(**response_data.json()), response)
    return {
        'response': response_data.status_code,
        'data': response_data.json()
    }
