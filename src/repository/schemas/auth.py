from src.repository.schemas import BaseSchema


class RegisterUserSchema(BaseSchema):
    username: str
    email: str
    password: str
    repeated_password: str


class SingInUserSchema(BaseSchema):
    username: str
    password: str


class UserTokenSchema(BaseSchema):
    access_token: str
    refresh_token: str


