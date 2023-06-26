from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.core.config import settings
from app.core.security import SECRET_KEY, ALGORITHM
from app.db.session import SessionLocal
from app.models.user import User
from app import cruds

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_PREFIX}/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = payload.get("sub")
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials."
        )
    user = cruds.user.get(username, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )
    return user
