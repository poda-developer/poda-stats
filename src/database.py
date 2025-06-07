import os
from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

engine = create_engine(os.environ.get("DATABASE_URL"))