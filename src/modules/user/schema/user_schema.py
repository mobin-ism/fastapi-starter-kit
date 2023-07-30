from datetime import datetime
from pydantic import BaseModel

# THIS CLASSES DEFINES THE RESPONSE TYPE OF USER

class UserBase(BaseModel):
    email: str
    profilePictureUrl: str
    phoneNumber: str
    role: str
    is_active: bool

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True