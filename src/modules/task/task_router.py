from fastapi import APIRouter, Path

router = APIRouter()

@router.get('/')
def getTasks():
    return "Get all the tasks"

@router.get('/{task_id}')
def getTaskById(task_id: int = Path(..., description = "Getting a specific task")):
    return "Get all the tasks"

@router.patch('/{task_id}')
def updateTask(task_id: int = Path(..., description = "Getting a specific task")):
    return "Update task {task_id}"


@router.delete('/{task_id}')
def deleteTask(task_id: int = Path(..., description = "Getting a specific task")):
    return "Delete task {task_id}"