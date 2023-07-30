from fastapi import APIRouter, Path
from fastapi import Depends, HTTPException
from src.config.db.db_config import async_get_db 
from src.modules.user.dto.create_user_dto import CreateUserDto
from sqlalchemy.ext.asyncio import AsyncSession
from src.modules.user.user_service import UserService
from src.modules.user.schema.user_schema import UserResponse
router = APIRouter()

@router.post('/')
async def createUser(createUserDto: CreateUserDto, db: AsyncSession = Depends(async_get_db)):
    return await UserService.create_user(db=db, createUserDto=createUserDto)

@router.get('/')
def getAllUsers():
    return "Get all the users"

@router.get('/{user_id}', summary="Get a specific user")
def getOneUser(user_id: int = Path(..., description="User ID")):
    return "Get user with ID: {user_id}"

@router.patch('/{user_id}', summary="Update a specific user")
def updateUser(user_id: int = Path(..., description="User ID")):
    return "Update User {user_id}"

@router.delete('/{user_id}', summary="Delete a specific user")
def deleteUser(user_id: int = Path(..., description="User ID")):
    return "Delete User {user_id}"
