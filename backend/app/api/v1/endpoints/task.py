from typing import List, Optional

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app import cruds
from app.api.depends import get_db, get_current_user
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse


router = APIRouter()


@router.post("/tasks", response_model=TaskResponse)
def create(
        obj_in: TaskCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.task.create(obj_in, current_user.username, db)


@router.get("/tasks/{task_id}", response_model=Optional[TaskResponse])
def get(
        task_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.task.get(task_id, db)


@router.get("/tasks", response_model=List[TaskResponse])
def get_multi(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.task.get_multi(db)


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update(
        task_id: int,
        obj_in: TaskUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.task.update(task_id, obj_in, current_user.username, db)


@router.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete(
        task_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    cruds.task.delete(task_id, current_user.username, db)


@router.put("/tasks/{task_id}/completed", response_model=TaskResponse)
def toggle_completed(
        task_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.task.toggle_completed(task_id, current_user.username, db)
