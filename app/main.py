from fastapi import FastAPI

from app.routers import post, user, auth

from .database import models
from .database.db import engine

models.BaseModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)

