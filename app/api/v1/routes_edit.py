from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.edit import EditIn, EditOut
from app.db.session import get_db
from app.db import crud
from app.nlp.preprocess import clean_text
from app.services.openai_client import run_generation

router = APIRouter()

@router.post("/edit", response_model=EditOut)
def edit_doc(payload: EditIn, db: Session = Depends(get_db)):
    # Basic flow: accept edited text, run model to update suggestions/output
    clean = clean_text(payload.edited_text)
    prompt = f"User edited version. Improve formatting and fix grammar.\n\nInput:\n{clean}"
    final_output, tokens = run_generation(prompt)
    # store document
    crud.create_document(db, payload.id, role="edited", content=clean)
    crud.create_document(db, payload.id, role="final_output", content=final_output)
    return {"id": payload.id, "final_output": final_output}
