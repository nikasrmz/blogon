from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


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
    email: EmailStr


class UserCreateUpdate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]

