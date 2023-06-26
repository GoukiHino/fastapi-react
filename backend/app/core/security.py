import datetime

from passlib.context import CryptContext
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"])

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
EXPIRE_MINUTE = 60 * 24


def create_hashed_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(username: str) -> str:
    to_encode = {
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPIRE_MINUTE)
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
