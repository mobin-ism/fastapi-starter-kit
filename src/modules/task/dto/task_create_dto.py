from pydantic import BaseModel
from typing import Optional
from data.task_enum import TaskStatusEnum

class CreateTaskDto(BaseModel):
    name: str
    description: Optional[str] = ''
    age: int
    isActive: bool
    status: TaskStatusEnum = TaskStatusEnum.PENDING
