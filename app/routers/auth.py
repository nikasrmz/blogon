from fastapi import APIRouter

from schemas import UserLogIn

router = APIRouter()


@router.post("/login")
def log_in(cred: UserLogIn):
    pass