from fastapi import APIRouter, Request
from typing import List
from models.maintenance import Maintenance
from utils.security import validateuser, validateadmin
from controllers.maintenance import (
    get_all_maintenances,
    get_maintenance_by_id,
    create_maintenance,
    update_maintenance,
    deactivate_maintenance
)

router = APIRouter()


@router.get("/maintenances", response_model=List[Maintenance])
@validateuser
async def list_maintenances(request: Request):
    return await get_all_maintenances(request)

@router.get("/maintenances/{maintenance_id}", response_model=Maintenance)
@validateuser
async def get_maintenance_endpoint(request: Request, maintenance_id: str):
    return await get_maintenance_by_id(request, maintenance_id)

@router.post("/maintenances", response_model=Maintenance)
@validateadmin
async def create_maintenance_endpoint(request: Request, m: Maintenance):
    return await create_maintenance(request, m)

@router.put("/maintenances/{maintenance_id}", response_model=Maintenance)
@validateadmin
async def update_maintenance_endpoint(request: Request, maintenance_id: str, m: Maintenance):
    return await update_maintenance(request, maintenance_id, m)

@router.delete("/maintenances/{maintenance_id}", response_model=Maintenance)
@validateadmin
async def deactivate_maintenance_endpoint(request: Request, maintenance_id: str):
    return await deactivate_maintenance(request, maintenance_id)
