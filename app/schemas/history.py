from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class HistoryOut(BaseModel):
    request: Dict[str, Any]
    documents: List[Dict[str, Any]]
