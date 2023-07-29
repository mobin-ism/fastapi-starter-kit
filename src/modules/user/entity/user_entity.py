from enum import Enum as PyEnum
from sqlalchemy import Enum, Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from src.config.db.db_config import Base
from src.config.db.mixins import Timestamp

class UserRole(PyEnum):
    ADMIN = 'admin'
    USER = 'user'


class User(Timestamp, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index= True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    profilePictureUrl = Column(String(100), unique=True, index=True, nullable=False)
    phoneNumber = Column(String(100), unique=True, index=True, nullable=False)
    role =  Column(Enum(UserRole))
    tasks = relationship("Task", back_populates='assignee')