from fastapi import APIRouter

from app.api.v1.endpoints import login, user, project, task

router = APIRouter()
router.include_router(login.router, tags=["Login"])
router.include_router(user.router, tags=["User"])
router.include_router(project.router, tags=["Project"])
router.include_router(task.router, tags=["Task"])
