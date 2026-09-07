from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from repositories.lead import LeadRepository 
from core.database import get_db
from schemas.lead import LeadFilters

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/lead/{lead_public_id}')
async def get_lead_by_public_id(db: db_dependency, lead_public_id:UUID):
    lead_repository = LeadRepository()
    return lead_repository.get_lead_by_public_id(lead_public_id)
    

@router.get('/leads/')
async def get_leads(db: db_dependency, lead_filters: LeadFilters = Depends()):
    lead_repository = LeadRepository()
    return lead_repository.get_leads(lead_filters)


@router.post('/lead/')
async def create_lead():
    pass


@router.patch('/lead/{lead_public_id}')
async def update_lead():
    pass


@router.delete('/lead/{lead_public_id}')
async def delete_lead():
    pass
