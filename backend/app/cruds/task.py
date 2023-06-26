from typing import List, Optional, Type

from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def create(obj_in: TaskCreate, created_by_username: str, db: Session) -> Task:
    task = Task(
        project_id=obj_in.project_id,
        title=obj_in.title,
        description=obj_in.description,
        created_by=created_by_username
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get(task_id: int, db: Session) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()


def get_multi(db: Session) -> List[Type[Task]]:
    return db.query(Task).filter(Task.is_deleted == False).all()


def update(task_id: int, obj_in: TaskUpdate, updated_by_username: str, db: Session) -> Task:
    task = get(task_id, db)
    task.title = obj_in.title
    task.description = obj_in.description
    task.updated_by = updated_by_username
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def delete(task_id: int, updated_by_username: str, db: Session) -> Task:
    task = get(task_id, db)
    task.is_deleted = True
    task.updated_by = updated_by_username
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def toggle_completed(task_id: int, updated_by_username: str, db: Session) -> Task:
    task = get(task_id, db)
    task.is_completed = not task.is_completed
    task.updated_by = updated_by_username
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
