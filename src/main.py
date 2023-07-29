from fastapi import FastAPI

import sys
from pathlib import Path

# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent))

from modules.user.user_router import router as user_router
from modules.task.task_router import router as task_router

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
