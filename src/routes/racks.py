from fastapi import APIRouter, Depends

from src.service.racks import RacksService
from src.repository.schemas.racks import InputRacksSchema
from src.routes.dependencies import get_racks_repository

racks_router = APIRouter(
    prefix='/racks'
)


@racks_router.get('/get_rack')
async def get_rack(
        rack_id: int,
        racks_repository=Depends(get_racks_repository)
):
    rack_schema = await RacksService(racks_repository).get_obj_schema(rack_id)
    return rack_schema


@racks_router.get('/get_all_rack')
async def get_all_rack(
        racks_repository=Depends(get_racks_repository)
):
    rack_schemas_list = await RacksService(racks_repository).get_all_obj_schema()
    return rack_schemas_list


@racks_router.post('/set_rack')
async def set_rack(rack_schema: InputRacksSchema,
                   racks_repository=Depends(get_racks_repository)
                   ):
    rack_schema = await RacksService(racks_repository).set_obj_schema(rack_schema.__dict__)
    return rack_schema


@racks_router.put('/update_rack')
async def update_rack(rack_id: int,
                      rack_schema: InputRacksSchema,
                      racks_repository=Depends(get_racks_repository)
                      ):
    updated_rack_id = await RacksService(racks_repository).update_obj_schema(rack_id, rack_schema.__dict__)
    return {"rack_id": updated_rack_id}


@racks_router.delete('/delete_rack')
async def delete_rack(rack_id: int,
                      racks_repository=Depends(get_racks_repository)
                      ):
    deleted_rack_id = await RacksService(racks_repository).delete_obj_schema(rack_id)
    return {"rack_id": deleted_rack_id}


@racks_router.get('/occupied_racks')
async def get_occupied_racks(racks_repository=Depends(get_racks_repository)):
    racks = await RacksService(racks_repository).get_occupied_racks()
    return racks


@racks_router.get('/get_rack_with_max_size')
async def get_rack_with_max_size(racks_repository=Depends(get_racks_repository)):
    racks = await RacksService(racks_repository).get_rack_with_max_size()
    return racks
