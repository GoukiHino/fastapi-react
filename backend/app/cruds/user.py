from typing import List, Optional, Type

from sqlalchemy.orm import Session

from app.core.security import create_hashed_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def create(obj_in: UserCreate, created_by_username: str, db: Session) -> User:
    user = User(
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


def get(username: str, db: Session) -> Optional[User]:
    return db.query(User).filter(User.username == username, User.is_deleted == False).first()


def get_multi(db: Session) -> List[Type[User]]:
    return db.query(User).filter(User.is_deleted == False).all()


def update(username: str, obj_in: UserUpdate, updated_by_username: str, db: Session) -> User:
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


def delete(username: str, updated_by_username: str, db: Session) -> User:
    user = get(username, db)
    user.is_deleted = True
    user.updated_by = updated_by_username
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate(username: str, password: str, db: Session) -> Optional[User]:
    user = get(username, db)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
