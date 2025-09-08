from pydantic import BaseModel
from typing import Any, Dict

class TokenStats(BaseModel):
    prompt: int
    completion: int
    total: int
