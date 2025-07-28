from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from oauth2 import create_access_token
from app.utils import verify
from app.database.db import get_db
from app.database.models import UserModel

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(credentials.username == UserModel.username).first()

    exception = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        )

    if not user:
        raise exception
    
    if not verify(credentials.password, user.password):
        raise exception
    
    access_token = create_access_token({"user_id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}