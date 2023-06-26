from typing import List, Optional, Type

from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


def create(obj_in: ProjectCreate, created_by_username: str, db: Session) -> Project:
    project = Project(
        title=obj_in.title,
        description=obj_in.description,
        created_by=created_by_username
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get(project_id: int, db: Session) -> Optional[Project]:
    return db.query(Project).filter(Project.id == project_id, Project.is_deleted == False).first()


def get_multi(db: Session) -> List[Type[Project]]:
    return db.query(Project).filter(Project.is_deleted == False).all()


def update(project_id: int, obj_in: ProjectUpdate, updated_by_username: str, db: Session) -> Project:
    project = get(project_id, db)
    project.title = obj_in.title
    project.description = obj_in.description
    project.updated_by = updated_by_username
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def delete(project_id: int, updated_by_username: str, db: Session) -> Project:
    project = get(project_id, db)
    project.is_deleted = True
    project.updated_by = updated_by_username
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def toggle_completed(project_id: int, updated_by_username: str, db: Session) -> Project:
    project = get(project_id, db)
    project.is_completed = not project.is_completed
    project.updated_by = updated_by_username
    db.add(project)
    db.commit()
    db.refresh(project)
    return project
