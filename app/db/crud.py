from sqlalchemy.orm import Session
from app.db import models
from datetime import datetime
import uuid

def create_request(db: Session, endpoint: str, model: str, tokens: dict):
    req = models.Request(
        id=str(uuid.uuid4()),
        endpoint=endpoint,
        model=model,
        prompt_tokens=tokens.get("prompt", 0),
        completion_tokens=tokens.get("completion", 0),
        total_tokens=tokens.get("total", 0),
        created_at=datetime.utcnow(),
    )
    db.add(req)
    db.commit()
    db.refresh(req)
    return req

def create_document(db: Session, request_id: str, role: str, content: str):
    doc = models.Document(
        id=str(uuid.uuid4()),
        request_id=request_id,
        role=role,
        content=content
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def get_request_with_docs(db: Session, request_id: str):
    req = db.get(models.Request, request_id)
    if not req:
        return None
    docs = db.query(models.Document).filter(models.Document.request_id == request_id).all()
    return {"request": req, "documents": docs}
