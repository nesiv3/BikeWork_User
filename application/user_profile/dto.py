from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

class UserProfileSchema(BaseModel):
    email: str
    birthdate: Optional[date]
    gender: Optional[str]
    address_line1: Optional[str]
    address_line2: Optional[str]
    city: str
    country: Optional[str]
    emergency_contact_name: Optional[str]
    emergency_contact_phone: Optional[str]
    avatar_url: Optional[str]
    phone_number: str

    class Config:
        from_attributes = True
        orm_mode = True














