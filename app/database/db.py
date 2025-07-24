import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('BLOGON_DB_USER')}:"
    f"{os.getenv('BLOGON_DB_PASS')}@"
    f"{os.getenv('BLOGON_DB_HOST')}:"
    f"{os.getenv('BLOGON_DB_PORT')}/"
    f"{os.getenv('BLOGON_DB_NAME')}"
)

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
