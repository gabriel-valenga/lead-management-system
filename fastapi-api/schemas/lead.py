from datetime import datetime
from pydantic import BaseModel, Field


class LeadFilters(BaseModel):
    email: str | None = Field(default=None, description='lead email')
    source: str | None = Field(default=None, description='source (where the lead came from)')
    name: str | None = Field(default=None, description='filter by lead first name or last name')
    first_name: str | None = Field(default=None, description='lead first name')
    last_name: str | None = Field(default=None, description='lead last name')
    created_at__gte: datetime | None = Field(
        default=None, description='lead creation datetime filtering by greather than or equal'
    )
    created_at__lte: datetime | None = Field(
        default=None, description='lead creation datetime filtering by less than or equal'
    )


class LeadCreateRequest(BaseModel):
    first_name: str = Field(min_length=2, max_length=20)
    last_name: str = Field(min_length=2, max_length=40)
    email: str = Field(min_length=)
