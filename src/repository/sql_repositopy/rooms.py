from sqlalchemy import select, func

from src.repository.sql_repositopy import BaseSQLRepository
from src.service import RoomsRepositoryInterface
from src.repository.sql_repositopy.models import RackORM, RoomORM
from src.repository.schemas.rooms import OutputRoomsSchema, RoomsWithOccupiedRackSchema


class RoomsRepository(BaseSQLRepository, RoomsRepositoryInterface):
    model = RoomORM
    schema = OutputRoomsSchema

    async def get_room_with_occupied_racks(self) -> list[RoomsWithOccupiedRackSchema]:
        rooms = []
        query = (
            select(
                RoomORM.id,
                RoomORM.name,
                func.array_agg(RackORM.id).label('racks')
            )
            .join(RoomORM.racks)
            .group_by(RoomORM.id)
            .where(RackORM.state == 'occupied')
        )
        racks_row = await self.session.execute(query)
        if not racks_row:
            raise Exception(f'{self.model.__name__} with id {self.model.id} not found.')
        for row in racks_row:
            room = {
                'room_id': row.id,
                'room_name': row.name,
                'racks_id': row.racks,
            }
            rooms.append(RoomsWithOccupiedRackSchema.model_validate(room))
        return rooms
