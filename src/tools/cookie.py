from fastapi import Request, Response

from src.repository.schemas.auth import UserTokenSchema


class CookieTools():

    @staticmethod
    async def set_tokens_to_cookie(user_token_schema: UserTokenSchema, response: Response):
        response.set_cookie('access_token', user_token_schema.access_token)
        response.set_cookie('refresh_token', user_token_schema.refresh_token)

    @staticmethod
    async def get_tokens_from_cookie(request: Request):
        access_token = request.cookies.get('access_token')
        refresh_token = request.cookies.get('refresh_token')
        return UserTokenSchema(**{
            'access_token': access_token,
            'refresh_token': refresh_token
        })
