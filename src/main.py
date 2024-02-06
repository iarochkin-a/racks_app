from fastapi import FastAPI
from src.routes.router import auth_app, racks_app, calculator_app


app = FastAPI(root_path='/api/v1')
app.mount('/auth', auth_app)
app.mount('/racks', racks_app)
app.mount('/calculator', calculator_app)


