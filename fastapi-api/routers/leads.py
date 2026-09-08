from typing import Annotated
from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from uuid import UUID
from repositories.lead import LeadRepository 
from core.database import get_db
from models.lead import Lead as LeadModel
from schemas.lead import LeadCreateRequest, LeadUpdateRequest, LeadFilters, LeadResponse

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/lead/{lead_public_id}')
async def get_lead_by_public_id(db: db_dependency, lead_public_id:UUID):
    lead_repository = LeadRepository()
    lead = lead_repository.get_lead_by_public_id(lead_public_id)
    return LeadResponse.model_validate(lead)
    

@router.get('/leads/')
async def get_leads(db: db_dependency, lead_filters: LeadFilters = Depends()):
    lead_repository = LeadRepository()
    leads = lead_repository.get_leads(lead_filters)
    return {"leads": [LeadResponse.model_validate(lead) for lead in leads]}


@router.post('/lead/')
async def create_lead(db: db_dependency, lead_create_request: LeadCreateRequest):
    lead_repository = LeadRepository()
    lead = LeadModel(**lead_create_request.model_dump())
    lead_repository.create_lead(lead)
    return LeadResponse.model_validate(lead)


@router.patch('/lead/{lead_public_id}')
async def update_lead(lead_update_request: LeadUpdateRequest, lead_public_id: int = Path(gt=0)):
    lead_repository = LeadRepository()
    lead = lead_repository.get_lead_by_public_id(lead_public_id)

    


@router.delete('/lead/{lead_public_id}')
async def delete_lead():
    pass
