from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from app.db.base_class import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_by = Column(String, ForeignKey("users.username"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=current_timestamp())
    updated_by = Column(String, ForeignKey("users.username"))
    updated_at = Column(DateTime, onupdate=current_timestamp())

    created_by_user = relationship("User", foreign_keys=created_by)
    updated_by_user = relationship("User", foreign_keys=updated_by)

    project = relationship("Project", back_populates="tasks")
