from src.repository.schemas import BaseSchema


class InputCustomersSchema(BaseSchema):
    name: str


class OutputCustomersSchema(InputCustomersSchema):
    id: int


class InputRoomsSchema(BaseSchema):
    name: str


class OutputRoomsSchema(InputRoomsSchema):
    id: int


class InputRacksSchema(BaseSchema):
    name: str
    size: int
    state: str
    customer_id: int
    room_id: int


class OutputRacksSchema(InputRacksSchema):
    id: int
    customer: "OutputCustomersSchema"
    room: "OutputRoomsSchema"


class OccupiedRacksSchema(BaseSchema):
    rack_id: int
    rack_name: str
    customer_name: str
    room_name: str


class MaxRackSizeInRoom(BaseSchema):
    room_id: int
    rack_id: int
    max_size: int
