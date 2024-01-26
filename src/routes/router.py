from src.routes.racks import racks_router
from src.routes.rooms import rooms_router
from src.routes.customers import customers_router
from src.routes.calculator import calculator_router
from fastapi import APIRouter


def get_router() -> [APIRouter]:
    return [racks_router, rooms_router, customers_router, calculator_router]