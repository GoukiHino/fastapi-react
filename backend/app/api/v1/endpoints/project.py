from typing import List, Optional

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app import cruds
from app.api.depends import get_db, get_current_user
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse


router = APIRouter()


@router.post("/projects", response_model=ProjectResponse)
def create(
        obj_in: ProjectCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.project.create(obj_in, current_user.username, db)


@router.get("/projects/{project_id}", response_model=Optional[ProjectResponse])
def get(
        project_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.project.get(project_id, db)


@router.get("/projects", response_model=List[ProjectResponse])
def get_multi(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.project.get_multi(db)


@router.put("/projects/{project_id}", response_model=ProjectResponse)
def update(
        project_id: int,
        obj_in: ProjectUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.project.update(project_id, obj_in, current_user.username, db)


@router.delete("/projects/{project_id}", response_model=ProjectResponse)
def delete(
        project_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    cruds.project.delete(project_id, current_user.username, db)


@router.put("/projects/{project_id}/completed", response_model=ProjectResponse)
def toggle_completed(
        project_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.project.toggle_completed(project_id, current_user.username, db)
