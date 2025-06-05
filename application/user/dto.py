from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

from application.user_profile.dto import UserProfileSchema
from application.user_role.dto import UserRoleSchema


class UserSchema(BaseModel):
    id: str
    full_name: Optional[str]
    is_verified: bool
    #created_at: datetime
    #updated_at: datetime
    profile: Optional[UserProfileSchema]
    roles: List[UserRoleSchema] = []

    class Config:
        from_attributes = True
        orm_mode = True