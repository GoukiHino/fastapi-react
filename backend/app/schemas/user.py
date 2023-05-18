import datetime
from typing import Optional

from app.schemas.user_base import UserBase


class UserCreate(UserBase):
    username: str
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserResponse(UserBase):
    is_deleted: bool
    created_by: str
    created_at: datetime.datetime
    updated_by: Optional[str] = None
    updated_at: Optional[datetime.datetime] = None

    created_by_user: UserBase
    updated_by_user: Optional[UserBase] = None
