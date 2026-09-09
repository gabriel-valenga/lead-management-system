from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path
from uuid import UUID
from repositories.lead import LeadRepository, get_lead_repository
from models.lead import Lead as LeadModel
from schemas.lead import LeadCreateRequest, LeadListResponse, LeadUpdateRequest, LeadFilters, LeadResponse

router = APIRouter()


@router.get('/lead/{lead_public_id}', response_model=LeadResponse)
def get_lead_by_public_id(
    lead_public_id:UUID,
    lead_repository: Annotated[LeadRepository, Depends(get_lead_repository)]
):
    lead = lead_repository.get_lead_by_public_id(lead_public_id)
    return lead
    

@router.get('/leads/', response_model=LeadListResponse)
def get_leads(
    lead_filters: Annotated[LeadFilters, Depends()],
    lead_repository: Annotated[LeadRepository, Depends(get_lead_repository)]
):
    leads = lead_repository.get_leads(lead_filters)
    return {"leads": leads}


@router.post('/lead/', response_model=LeadResponse)
def create_lead(
    lead_create_request: LeadCreateRequest,
    lead_repository: Annotated[LeadRepository, Depends(get_lead_repository)]
):
    lead = LeadModel(**lead_create_request.model_dump())
    created_lead = lead_repository.create_lead(lead)
    return created_lead


@router.patch('/lead/{lead_public_id}', response_model=LeadResponse)
def update_lead(
    lead_update_request: LeadUpdateRequest, 
    lead_public_id: Annotated[UUID, Path(gt=0)], #editing right here UUID use, check if its possible...
    lead_repository: Annotated[LeadRepository, Depends(get_lead_repository)]
):
    lead = lead_repository.get_lead_by_public_id(lead_public_id)
    if not lead:
        raise HTTPException(status_code=404, detail='lead not found')
    updated_lead = lead_repository.update_lead(lead, lead_update_request)
    return updated_lead

    
@router.delete('/lead/{lead_public_id}')
def delete_lead():
    pass
