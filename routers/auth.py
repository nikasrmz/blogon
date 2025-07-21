from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register():
    pass


@router.post("/login")
def log_in():
    pass