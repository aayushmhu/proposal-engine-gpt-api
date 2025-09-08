from pydantic import BaseModel
from typing import Dict, Any, Optional, List

class ProcessIn(BaseModel):
    text: str
    options: Optional[Dict[str, Any]] = None

class ProcessOut(BaseModel):
    id: str
    suggestions: List[str] = []
    final_output: str
    metadata: Dict[str, Any] = {}
    token_stats: Dict[str, Any] = {}
