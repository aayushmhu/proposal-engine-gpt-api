from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import crud
from app.schemas.history import HistoryOut

router = APIRouter()

@router.get("/history/{request_id}", response_model=HistoryOut)
def get_history(request_id: str, db: Session = Depends(get_db)):
    result = crud.get_request_with_docs(db, request_id)
    if not result:
        raise HTTPException(status_code=404, detail="request not found")
    # simple serialization
    req = result["request"].__dict__.copy()
    req.pop("_sa_instance_state", None)
    docs = []
    for d in result["documents"]:
        di = d.__dict__.copy()
        di.pop("_sa_instance_state", None)
        docs.append(di)
    return {"request": req, "documents": docs}
