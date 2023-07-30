from enum import Enum as PyEnum
from sqlalchemy import Enum, Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from src.config.db.db_config import Base
from src.config.db.mixins import Timestamp

class Priority(PyEnum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class Task(Timestamp, Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index= True)
    title = Column(String(100), unique=True, index=True, nullable=False)
    descripttion = Column(Text, nullable=True)
    priority = Column(Enum(Priority), default=Priority.LOW)
    assignedTo = Column(Integer, ForeignKey("users.id"), nullable=False)
    # assignee = relationship("User", back_populates='tasks')