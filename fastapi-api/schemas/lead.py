from datetime import datetime
from pydantic import BaseModel, Field

class LeadFilters(BaseModel):
    email: str | None = Field(default=None, description='lead email')
    source: str | None = Field(default=None, description='source (where the lead came from)')
    name: str | None = Field(default=None, description='filter by lead first name or last name')
    first_name: str | None = Field(default=None, description='lead first name')
    last_name: str | None = Field(default=None, description='lead last name')
    created_at: datetime | None = Field(default=None, description='lead creation date')
