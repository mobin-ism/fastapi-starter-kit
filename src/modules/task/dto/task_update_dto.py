from pydantic import BaseModel
from typing import Optional
from data.task_enum import TaskStatusEnum
from task_create_dto import CreateTaskDto

class UpdateTaskDto(CreateTaskDto):
    pass
