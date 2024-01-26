from src.repository.schemas import BaseSchema


class InputRoomsSchema(BaseSchema):
    name: str


class OutputRoomsSchema(InputRoomsSchema):
    id: int
    racks: list["OutputRacksSchema"]


class InputCustomersSchema(BaseSchema):
    name: str


class OutputCustomersSchema(InputCustomersSchema):
    id: int
    racks: list["OutputRacksSchema"]


class InputRacksSchema(BaseSchema):
    name: str
    size: int
    state: str
    customer_id: int
    room_id: int


class OutputRacksSchema(InputRacksSchema):
    id: int


class RoomsWithOccupiedRackSchema(BaseSchema):
    room_id: int
    room_name: str
    racks_id: list[int]
