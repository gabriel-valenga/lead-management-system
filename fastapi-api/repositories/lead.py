from sqlalchemy import select
from sqlalchemy.orm import Session
from models.lead import Lead
from schemas.lead import LeadFilters
from uuid import UUID


class LeadRepository:

    def __init__(self, db: Session):
        self.db = db


    def get_lead_by_public_id(self, lead_public_id: UUID):
        query = select(Lead).where(Lead.public_id==lead_public_id)
        result = self.db.execute(query)
        return result.scalar_one_or_none()


    def get_leads(self, filters:LeadFilters):
        query = select(Lead)
        query_filters = None
        if filters.email:
            query_filters
        result = self.db.execute(query)
        return result.scalars().all()