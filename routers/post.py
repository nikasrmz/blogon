from fastapi import APIRouter, Response, status, HTTPException
from random import randint

from schemas import PostCreateUpdate
from database.dummy import posts


router = APIRouter()


def find_post_index(id: int) -> int:
    for idx, post in enumerate(posts):
        if post["id"] == id:
            return idx



@router.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreateUpdate):
    post_dict = post.model_dump()
    post_dict["id"] = randint(1, 10_000_000)
    posts.append(post_dict)
    return {"data": post_dict}


@router.get("/posts")
def get_all_posts():
    return {"data": posts}


@router.get("/posts/{id}")
def get_post(id: int):
    idx = find_post_index(id)

    if not idx:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )
    
    return {"data": posts[idx]}


@router.put("/posts/{id}")
def update_post(id: int, post: PostCreateUpdate):
    idx = find_post_index(id)

    if not idx:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    del posts[idx]
    post_dict = post.model_dump()
    post_dict["id"] = id
    posts.append(post_dict)
    return {"data": f"post with id: {id} updated"}
    

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    idx = find_post_index(id)

    if not idx:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    del posts[idx]
    return {"detail": f"post with id: {id} deleted"}
    