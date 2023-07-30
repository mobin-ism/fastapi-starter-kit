from sqlalchemy import Enum, Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from src.config.db.db_config import Base
from src.config.db.mixins import Timestamp
from src.modules.user.data.user_role_enum import UserRole

class User(Timestamp, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index= True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    profilePictureUrl = Column(String(100), index=True, nullable=False)
    phoneNumber = Column(String(100), index=True, nullable=False)
    role =  Column(Enum(UserRole), default=UserRole.USER)
    is_active = Column(Boolean, default=True)
    # tasks = relationship("Task", back_populates='assignee')