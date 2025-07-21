from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
def get_all_users():
    pass


@router.get("/users/{user_id}")
def get_user(user_id: int):
    pass


@router.post("/users")
def create_new_user():
    pass


@router.put("/users/{user_id}")
def update_user(user_id: int):
    pass


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    pass