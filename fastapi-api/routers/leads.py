from fastapi import APIRouter
from uuid import UUID

router = APIRouter()


@router.get('/lead/{lead_public_id}')
async def get_lead_by_public_id(lead_public_id:UUID):
    pass


@router.get('/leads/')
async def get_leads():
    pass


@router.post('/lead/')
async def create_lead():
    pass


@router.patch('/lead/{lead_public_id}')
async def update_lead():
    pass


@router.delete('/lead/{lead_public_id}')
async def delete_lead():
    pass
