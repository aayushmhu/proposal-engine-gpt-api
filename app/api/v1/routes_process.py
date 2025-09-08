from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.process import ProcessIn, ProcessOut
from app.db.session import get_db
from app.nlp.preprocess import clean_text
from app.services.openai_client import run_generation
from app.nlp.token_utils import count_tokens
from app.db import crud
from app.services.cost_estimator import estimate_cost

router = APIRouter()

@router.post("/process", response_model=ProcessOut)
def process_doc(payload: ProcessIn, db: Session = Depends(get_db)):
    # 1. Clean input
    clean = clean_text(payload.text)

    # 2. Count tokens for prompt
    prompt_tokens = count_tokens(clean)

    # 3. Nudge model to produce suggestions + final output via prompt template
    prompt = f"Improve and restructure the following RFP/Proposal. Provide a short list of suggestions, then a cleaned final output.\n\nInput:\n{clean}"

    # 4. Call AI
    final_output, tokens = run_generation(prompt)

    # 5. Estimate cost
    cost = estimate_cost(tokens.get("prompt", 0), tokens.get("completion", 0), "gpt-3.5-turbo")

    # 6. Store request and documents
    request = crud.create_request(db, endpoint="/process", model="gpt-3.5-turbo", tokens={"prompt": tokens.get("prompt",0), "completion": tokens.get("completion",0), "total": tokens.get("total",0)})
    crud.create_document(db, request.id, role="input", content=payload.text)
    crud.create_document(db, request.id, role="final_output", content=final_output)

    # 7. Build metadata (simple)
    metadata = {
        "sections": [],
        "keywords": []
    }

    return {
        "id": str(request.id),
        "suggestions": ["See final output"],
        "final_output": final_output,
        "metadata": metadata,
        "token_stats": {"prompt": tokens.get("prompt",0), "completion": tokens.get("completion",0), "total": tokens.get("total",0), "cost_estimate": cost}
    }
