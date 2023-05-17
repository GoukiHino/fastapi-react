from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    password = Column(String, nullable=False)
    display_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_by = Column(String, ForeignKey("users.username"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=current_timestamp())
    updated_by = Column(String, ForeignKey("users.username"))
    updated_at = Column(DateTime, onupdate=current_timestamp())

    created_by_user = relationship("User", foreign_keys=created_by, remote_side=username)
    updated_by_user = relationship("User", foreign_keys=updated_by, remote_side=username)
