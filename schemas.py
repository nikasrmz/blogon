from pydantic import BaseModel

class UserCreate(BaseModel):

    username: str
    email: str
    password: str


class UserLogIn(BaseModel):

    username: str
    password: str


class PostCreate(BaseModel):

    title: str
    content: str
    category: str



    
