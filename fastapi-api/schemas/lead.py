from pydantic import BaseModel, Field

class LeadFilters(BaseModel):
    email: str | None = Field(default=None, description='email field')
    source: str = None | None
    name: str | None #filter first_name or last_name
    first_name: str = None | None
    last_name: str = None | None
