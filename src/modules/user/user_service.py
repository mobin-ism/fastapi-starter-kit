from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.modules.user.schema.user_entity import User
from src.modules.user.dto.create_user_dto import CreateUserDto

class UserService():

    async def create_user(db: AsyncSession, createUserDto: CreateUserDto):
        db_user = User(email=createUserDto.email, profilePictureUrl=createUserDto.profilePictureUrl, phoneNumber=createUserDto.phoneNumber, is_active=createUserDto.is_active)
                
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user