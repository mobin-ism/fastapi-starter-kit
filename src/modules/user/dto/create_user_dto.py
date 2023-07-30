from pydantic import BaseModel
from typing import Optional
from src.modules.user.schema.user_schema import UserBase

class CreateUserDto(UserBase):
    ...
