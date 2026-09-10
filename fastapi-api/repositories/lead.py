from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from core.database import get_db
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
        query_filters = []
        if filters.email:
            query_filters.append(Lead.email==filters.email)
        if filters.source:
            query_filters.append(Lead.source.icontains(filters.source))
        if filters.name:
            query_filters.append(Lead.first_name.icontains(filters.name))
            query_filters.append(Lead.last_name.icontains(filters.name))
        else:
            if filters.first_name:
                query_filters.append(Lead.first_name.icontains(filters.first_name))
            if filters.last_name:
                query_filters.append(Lead.last_name.icontains(filters.last_name))
        if filters.created_at__gte:
            query_filters.append(Lead.created_at <= filters.created_at__gte)
        elif filters.created_at__lte:
            query_filters.append(Lead.created_at >= filters.created_at__lte)
        result = self.db.execute(query.where(*query_filters))
        return result.scalars().all()


    def create_lead(self, lead:Lead):
        self.db.add(lead)
        self.db.commit()
        return lead


    def update_lead(self, lead:Lead, data:dict):
        for field, value in data.items():
            setattr(lead, field, value)
        self.db.commit()
        return lead


    def delete_lead(self, lead:Lead):
        self.db.delete(lead)
        self.db.commit()


def get_lead_repository(db:Session = Depends(get_db)) -> LeadRepository:
    return LeadRepository(db)
