from typing import List, Optional, Type

from sqlalchemy.orm import Session

from app import models, schemas
from app.core.security import create_hashed_password


def create(obj_in: schemas.UserCreate, created_by_username: str, db: Session) -> models.User:
    user = models.User(
        username=obj_in.username,
        password=create_hashed_password(obj_in.password),
        diplay_name=obj_in.display_name,
        email=obj_in.email,
        created_by=created_by_username
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get(username: str, db: Session) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.username == username, models.User.is_deleted == False).first()


def get_multi(db: Session) -> List[Type[models.User]]:
    return db.query(models.User).filter(models.User.is_deleted == False).all()


def update(username: str, obj_in: schemas.UserUpdate, updated_by_username: str, db: Session) -> models.User:
    user = get(username, db)
    if obj_in.password:
        user.password = create_hashed_password(obj_in.password)
    user.display_name = obj_in.display_name
    user.email = obj_in.email
    user.updated_by = updated_by_username
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete(username: str, updated_by_username: str, db: Session) -> models.User:
    user = get(username, db)
    user.is_deleted = True
    user.updated_by = updated_by_username
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
