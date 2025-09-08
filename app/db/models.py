import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from app.db.base import Base

# Use UUID for Postgres, but on SQLite it will be text
def _uuid_default():
    return str(uuid.uuid4())

class Request(Base):
    __tablename__ = "requests"
    id = Column(String, primary_key=True, default=_uuid_default)
    endpoint = Column(String, nullable=False)
    model = Column(String, nullable=False)
    prompt_tokens = Column(Integer, nullable=True)
    completion_tokens = Column(Integer, nullable=True)
    total_tokens = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Document(Base):
    __tablename__ = "documents"
    id = Column(String, primary_key=True, default=_uuid_default)
    request_id = Column(String, nullable=False)
    role = Column(String, nullable=False)  # input, ai_suggestions, final_output, edited
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
