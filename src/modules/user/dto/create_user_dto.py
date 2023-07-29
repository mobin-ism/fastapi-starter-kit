from pydantic import BaseModel
from typing import Optional

class CreateUserDto(BaseModel):
    name: str
    bio: Optional[str] = ''
    age: int
    isActive: bool
