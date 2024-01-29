from src.repository.schemas import BaseSchema


class InputCalculatorSchema(BaseSchema):
    variables: list[int]
    is_reverse: bool


class OutputCalculatorSchema(BaseSchema):
    variables: list[int]
    result: int | float
