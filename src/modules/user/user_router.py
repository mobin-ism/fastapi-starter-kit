from fastapi import APIRouter, Path

router = APIRouter()

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
