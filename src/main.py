from fastapi import FastAPI

import sys
from pathlib import Path

# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent))

from src.modules.user.user_router import router as user_router
from src.modules.task.task_router import router as task_router

from src.config.db.db_config import engine, Base
from src.modules.task.entity.task_entity import Task
from src.modules.user.schema.user_entity import User

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Starter Kit Of FastAPI",
    description="This is just a bare minimum code base for getting started with FastAPI.",
    version="0.0.1",
    contact={
        "name": "mobinism",
        "github": "@mobin-ism",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(user_router, prefix='/user', tags=['User Endpoints'])
app.include_router(task_router, prefix='/task', tags=['Task Endpoints'])
