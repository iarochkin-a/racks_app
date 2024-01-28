from fastapi import APIRouter, Depends

from src.service.rooms import RoomsService
from src.repository.schemas.rooms import InputRoomsSchema
from src.routes.dependencies import get_rooms_repository

rooms_router = APIRouter(
    prefix='/rooms'
)


@rooms_router.get('/get_room')
async def get_room(
        room_id: int,
        rooms_repository=Depends(get_rooms_repository)
):
    rooms_schema = await RoomsService(rooms_repository).get_obj_schema(room_id)
    return rooms_schema


@rooms_router.get('/get_all_rooms')
async def get_all_rooms(rooms_repository=Depends(get_rooms_repository)):
    room_schemas = await RoomsService(rooms_repository).get_all_obj_schema()
    return room_schemas


@rooms_router.post('/set_room')
async def set_room(room_schema: InputRoomsSchema,
                   rooms_repository=Depends(get_rooms_repository)
                   ):
    room_id = await RoomsService(rooms_repository).set_obj_schema(room_schema.__dict__)
    return {'room_id': room_id}


@rooms_router.put('/update_room')
async def update_rack(room_id: int,
                      room_schema: InputRoomsSchema,
                      rooms_repository=Depends(get_rooms_repository)
                      ):
    updated_room_id = await RoomsService(rooms_repository).update_obj_schema(room_id, room_schema.__dict__)
    return {"updated_room_id": updated_room_id}


@rooms_router.delete('/delete_room')
async def delete_rack(room_id: int,
                      rooms_repository=Depends(get_rooms_repository)
                      ):
    deleted_room_id = await RoomsService(rooms_repository).delete_obj_schema(room_id)
    return {"deleted_room_id": deleted_room_id}


@rooms_router.get('/get_room_with_occupied_racks')
async def get_room_with_occupied_racks(rooms_repository=Depends(get_rooms_repository)):
    rooms_with_occupied_racks_schema = await RoomsService(rooms_repository).get_room_with_occupied_racks()
    return rooms_with_occupied_racks_schema
