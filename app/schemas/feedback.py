from pydantic import BaseModel

class FeedbackIn(BaseModel):
    request_id: str
    rating: int
    comment: str
