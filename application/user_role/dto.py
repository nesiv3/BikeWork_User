from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

class UserRoleSchema(BaseModel):
    role_catalog_id: str
    #assigned_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True









