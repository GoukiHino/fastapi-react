from typing import List, Optional, Type

from sqlalchemy.orm import Session

from app import models, schemas


def create(obj_in: schemas.ProjectCreate, created_by_username: str, db: Session) -> models.Project:
    project = models.Project(
        title=obj_in.title,
        description=obj_in.description,
        created_by=created_by_username
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get(project_id: int, db: Session) -> Optional[models.Project]:
    return db.query(models.Project).filter(models.Project.id == project_id, models.Project.is_deleted == False).first()


def get_multi(db: Session) -> List[Type[models.Project]]:
    return db.query(models.Project).filter(models.Project.is_deleted == False).all()


def update(project_id: int, obj_in: schemas.ProjectUpdate, updated_by_username: str, db: Session) -> models.Project:
    project = get(project_id, db)
    project.title = obj_in.title
    project.description = obj_in.description
    project.updated_by = updated_by_username
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def delete(project_id: int, updated_by_username: str, db: Session) -> models.Project:
    project = get(project_id, db)
    project.is_deleted = True
    project.updated_by = updated_by_username
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def toggle_completed(project_id: int, updated_by_username: str, db: Session) -> models.Project:
    project = get(project_id, db)
    project.is_completed = not project.is_completed
    project.updated_by = updated_by_username
    db.add(project)
    db.commit()
    db.refresh(project)
    return project
