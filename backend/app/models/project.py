from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from app.db.base_class import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
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

    tasks = relationship("Task", back_populates="project")
