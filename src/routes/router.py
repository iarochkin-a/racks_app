from src.routes.racks import racks_router
from src.routes.rooms import rooms_router
from src.routes.customers import customers_router
from src.routes.calculator import calculator_router
from src.routes.auth import auth_router
from fastapi import FastAPI, Depends
from src.routes.dependencies import auth_middleware


auth_app = FastAPI()
auth_app.include_router(auth_router)

racks_app = FastAPI(root_path='/dcim', dependencies=[Depends(auth_middleware)])
racks_app.include_router(racks_router)
racks_app.include_router(rooms_router)
racks_app.include_router(customers_router)

calculator_app = FastAPI(dependencies=[Depends(auth_middleware)])
calculator_app.include_router(calculator_router)
