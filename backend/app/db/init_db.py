from app import models

from app.core.config import settings
from app.core.security import create_hashed_password

from app.db.session import SessionLocal

db = SessionLocal()
try:
    user = models.User(
        username=settings.INIT_USERNAME,
        password=create_hashed_password(settings.INIT_PASSWORD),
        display_name="Admin User",
        email=settings.INIT_EMAIL,
        created_by=settings.INIT_USERNAME
    )
    db.add(user)
    db.commit()
    db.refresh(user)
finally:
    db.close()
