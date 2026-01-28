import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL =", DATABASE_URL)

if not DATABASE_URL:
    raise Exception("DATABASE_URL not found. Check .env file")

engine = create_engine(DATABASE_URL)
Base = declarative_base()
