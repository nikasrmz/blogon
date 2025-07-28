import os
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import status, HTTPException, Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.schemas import TokenData
from app.database.db import get_db
from app.database.models import UserModel


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire

    token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return token


def verify_access_token(token: str, credentials_exception: Exception) -> TokenData:
    try:
        decoded = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id = decoded.get("user_id")
        if id is None:
            raise JWTError()
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Access Token", 
        headers={"WWW-Authenticate": "Bearer"}
    )

    token = verify_access_token(token, credentials_exception)

    user = db.query(UserModel).filter(UserModel.id == token.id).first()

    return user