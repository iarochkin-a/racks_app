from fastapi import FastAPI
from src.routes.router import get_router


app = FastAPI()
for route in get_router():
    app.include_router(router=route)
