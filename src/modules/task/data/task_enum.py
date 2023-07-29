from enum import Enum

class TaskStatusEnum(str, Enum):
    APPROVED = "approved"
    PENDING = "pending"
    ARCHIVED = "archived"
