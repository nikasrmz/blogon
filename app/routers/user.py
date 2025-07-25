from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.utils import hash
from app.database.db import get_db
from app.database.models import UserModel
from app.schemas import UserCreateUpdate, UserResponse


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_new_user(user: UserCreateUpdate, db: Session = Depends(get_db)):

    user.password = hash(user.password)
    new_user = UserModel(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(UserModel).filter(UserModel.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {id} not found",
        )
    
    return user


@router.put("/{id}", response_model=UserResponse)
def update_user(id: int, user: UserCreateUpdate, db: Session = Depends(get_db)):

    user.password = hash(user.password)
    user_query = db.query(UserModel).filter(UserModel.id == id)

    if not user_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {id} not found",
        )
    
    user_query.update(user.model_dump())
    db.commit()

    return user_query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):

    user_query = db.query(UserModel).filter(UserModel.id == id)

    if not user_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {id} not found",
        )
    
    user_query.delete()
    db.commit()
    