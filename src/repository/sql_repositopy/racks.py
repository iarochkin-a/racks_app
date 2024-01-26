from src.repository.sql_repositopy import BaseSQLRepository
from src.service import RacksRepositoryInterface
from src.repository.sql_repositopy.models import RackORM, CustomerORM, RoomORM
from src.repository.schemas.racks import OutputRacksSchema, OccupiedRacksSchema, MaxRackSizeInRoom
from sqlalchemy import select, func
from sqlalchemy.orm import Bundle


class RacksRepository(BaseSQLRepository, RacksRepositoryInterface):
    model = RackORM
    schema = OutputRacksSchema

    async def get_occupied_racks(self):
        racks = []
        query = (
            select(
                Bundle('racks', RackORM.id, RackORM.name),
                Bundle('customer', CustomerORM.name),
                Bundle('rooms', RoomORM.name)
            )
            .join(RackORM.customer)
            .join(RackORM.room)
            .where(RackORM.state == 'occupied')

        )
        racks_row = await self.session.execute(query)
        if not racks_row:
            raise Exception(f'{self.model.__name__} with id {self.model.id} not found.')
        for row in racks_row:
            rack = {
                'rack_id': row.racks.id,
                'rack_name': row.racks.name,
                'customer_name': row.customer.name_1,
                'room_name': row.rooms.name_2
            }
            racks.append(OccupiedRacksSchema.model_validate(rack))
        return racks

    async def get_rack_with_max_size(self):
        rooms = []
        query = (
            select(
                RoomORM.id,
                RackORM.id,
                func.max(RackORM.size).label('max_size')
            )
            .join(RoomORM)
            .group_by(RoomORM.id, RackORM.id)
            .order_by(RoomORM.id)
            .distinct(RoomORM.id)
        )

        racks_row = await self.session.execute(query)
        if not racks_row:
            raise Exception(f'{self.model.__name__} with id {self.model.id} not found.')
        for row in racks_row:
            room = {
                'room_id': row.id,
                'rack_id': row.id_1,
                'max_size': row.max_size,
            }
            rooms.append(MaxRackSizeInRoom.model_validate(room))
        return rooms
