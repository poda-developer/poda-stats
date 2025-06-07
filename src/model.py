from sqlmodel import Field, SQLModel, Session
from database import engine
from datetime import date

class Feedback(SQLModel, table=True):
    id: int = Field(primary_key=True)
    text: str = Field()
    createdAt: date = Field()
    name: str = Field(index=True)
    cycle: int = Field()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session