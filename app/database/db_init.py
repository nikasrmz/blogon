from db import engine
from models import BaseModel

def init_db():
    BaseModel.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
