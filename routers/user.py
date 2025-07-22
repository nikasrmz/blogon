from fastapi import APIRouter

from schemas import UserCreate

router = APIRouter()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    pass


@router.post("/users")
def create_new_user(user: UserCreate):
    pass


@router.put("/users/{user_id}")
def update_user(user_id: int):
    pass


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    pass