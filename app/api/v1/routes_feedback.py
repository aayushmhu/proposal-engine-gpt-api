from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.feedback import FeedbackIn
from app.db.session import get_db
from app.db import crud

router = APIRouter()

@router.post("/feedback")
def submit_feedback(payload: FeedbackIn, db: Session = Depends(get_db)):
    # For MVP, we simply store feedback as a Document with role 'feedback'
    crud.create_document(db, payload.request_id, role="feedback", content=f"rating:{payload.rating};comment:{payload.comment}")
    return {"ok": True}
