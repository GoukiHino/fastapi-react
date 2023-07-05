from typing import List, Optional

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app import cruds
from app.api.depends import get_db, get_current_user
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserResponse

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create(
        obj_in: UserCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.user.create(obj_in, current_user.username, db)


@router.get("/users/{username}", response_model=Optional[UserResponse])
def get(
        username: str,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.user.get(username, db)


@router.get("/users", response_model=List[UserResponse])
def get(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.user.get_multi(db)


@router.put("/users/{username}", response_model=UserResponse)
def update(
        username: str,
        obj_in: UserUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.user.update(username, obj_in, current_user.username, db)


@router.delete("/users/{username}", response_model=UserResponse)
def delete(
        username: str,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return cruds.user.delete(username, current_user.username, db)
