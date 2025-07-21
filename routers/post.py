from fastapi import APIRouter

router = APIRouter()


@router.get("/posts")
def get_all_posts():
    pass


@router.get("/posts/{post_id}")
def get_post(post_id: int):
    pass


@router.post("/posts")
def create_post():
    pass


@router.put("/posts/{post_id}")
def update_post(post_id: int):
    pass


@router.delete("/posts/{post_id}")
def delete_post(post_id: int):
    pass
