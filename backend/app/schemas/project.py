import datetime
from typing import Optional, List

from app.schemas.user_base import UserBase
from app.schemas.project_base import ProjectBase
from app.schemas.task_base import TaskBase


class ProjectCreate(ProjectBase):
    id: Optional[int] = None


class ProjectUpdate(ProjectBase):
    id: Optional[int] = None


class ProjectResponse(ProjectBase):
    is_completed: bool
    is_deleted: bool
    created_by: str
    created_at: datetime.datetime
    updated_by: Optional[str] = None
    updated_at: Optional[datetime.datetime] = None

    created_by_user: UserBase
    updated_by_user: Optional[UserBase] = None

    tasks: List[TaskBase] = []
