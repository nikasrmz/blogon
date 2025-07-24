from datetime import datetime
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreateUpdate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreateUpdate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class UserLogIn(BaseModel):

    username: str
    password: str

