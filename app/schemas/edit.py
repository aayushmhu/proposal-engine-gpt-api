from pydantic import BaseModel

class EditIn(BaseModel):
    id: str
    edited_text: str

class EditOut(BaseModel):
    id: str
    final_output: str
