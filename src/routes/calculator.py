from typing import Annotated
import http

from fastapi import APIRouter, Query

from src.service.calculator import CalculatorService


calculator_router = APIRouter(
    prefix='/calculator'
)


@calculator_router.get('/sum/')
async def sum(is_reverse: bool, num: int,  q: Annotated[list[int], Query()] = None):
    res = await CalculatorService(num, is_reverse).sum(q)
    return {'res': res}


@calculator_router.get('/minus')
async def minus(is_reverse: bool, num: int,  q: Annotated[list[int], Query()] = None):
    res = await CalculatorService(num, is_reverse).minus(q)
    return {'res': res}


@calculator_router.get('/product')
async def product(is_reverse: bool, num: int,  q: Annotated[list[int], Query()] = None):
    res = await CalculatorService(num, is_reverse).product(q)
    return {'res': res}


@calculator_router.get('/quotient')
async def quotient(is_reverse: bool, num: int,  q: Annotated[list[int], Query()] = None):
    try:
        res = await CalculatorService(num, is_reverse).quotient(q)
        return {'res': res}
    except ZeroDivisionError as error:
        return {
            'status': http.HTTPStatus.BAD_REQUEST,
            'error': error.args
        }

