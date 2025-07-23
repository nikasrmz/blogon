from fastapi import APIRouter, Response, status, HTTPException
from random import randint
from sqlalchemy import text

from app.schemas import PostCreateUpdate
from app.database.db import engine

conn = engine.connect()

router = APIRouter()

@router.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreateUpdate):
    post = conn.execute(
        text("insert into posts (title, content, published) values (:title, :content, :published) returning *"),
        {"title": post.title, "content": post.content, "published": post.published},
    ).mappings().fetchone()
    conn.commit()
    return {"created": dict(post)}


@router.get("/posts")
def get_all_posts():
    result = conn.execute(text("select * from posts")).mappings().fetchall()
    posts = [dict(row) for row in result]
    return {"data": posts}


@router.get("/posts/{id}")
def get_post(id: int):
    post = conn.execute(
        text("""select * from posts where id = :id"""),
        {"id": id},
    ).mappings().fetchone()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )
    
    return {"data": dict(post)}


@router.put("/posts/{id}")
def update_post(id: int, post: PostCreateUpdate):
    post = conn.execute(
        text("""update posts set title = :title, content = :content, published = :published where id = :id returning *"""),
        {"title": post.title, "content": post.content, "published": post.published, "id": id},
        ).mappings().fetchone()
    
    conn.commit()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    return {"updated": dict(post)}
    

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post = conn.execute(
        text("""delete from posts where id = :id returning *"""),
        {"id": id},
        ).mappings().fetchone()
    
    conn.commit()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    return {"deleted post": dict(post)}
    