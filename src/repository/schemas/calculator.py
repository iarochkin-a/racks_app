from src.repository.schemas import BaseSchema


class InputCalculatorSchema(BaseSchema):
    variables: list[int]
    is_reverse: bool
