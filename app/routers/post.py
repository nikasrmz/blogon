from typing import List

from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas import PostCreateUpdate, PostResponse, TokenData
from app.database.db import get_db
from app.database.models import PostModel
from oauth2 import get_current_user


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(
    post: PostCreateUpdate,
    db: Session = Depends(get_db), 
    user_id: TokenData = Depends(get_current_user),
):

    new_post = PostModel(**post.model_dump(), user_id=user_id.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/", response_model=List[PostResponse])
def get_all_posts(db: Session = Depends(get_db)):

    posts = db.query(PostModel).all()

    return posts


@router.get("/{id}", response_model=PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):

    post = db.query(PostModel).filter(PostModel.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )
    
    return post


@router.put("/{id}", response_model=PostResponse)
def update_post(
    id: int,
    post: PostCreateUpdate, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(get_current_user)
):

    post_query = db.query(PostModel).filter(PostModel.id == id)

    if not post_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )
    
    post_query.update(post.model_dump())
    db.commit()


    return post_query.first()
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int, 
    db: Session = Depends(get_db), 
    user_id: int = Depends(get_current_user)
):

    post_query = db.query(PostModel).filter(PostModel.id == id)

    if not post_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )
    
    post_query.delete()
    db.commit()
    