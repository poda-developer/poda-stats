from typing import Annotated
from datetime import datetime
from fastapi import Depends, FastAPI
from sqlmodel import Session, select
from model import get_session, create_db_and_tables, Feedback

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/feedbacks")
def record_feedback(feedback: Feedback, session: SessionDep) -> Feedback:
    feedback.createdAt = datetime.now()
    session.add(feedback)
    session.commit()
    session.refresh(feedback)
    return feedback

@app.get("/feedbacks")
def get_month_feedbacks(session: SessionDep) -> list[Feedback]:
    feedbacks = session.exec(select(Feedback).order_by(Feedback.createdAt.desc())).all()
    return feedbacks