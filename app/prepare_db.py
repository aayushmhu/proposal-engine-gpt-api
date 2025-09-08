from sqlalchemy import create_engine
from app.core.config import settings
from app.db.base import Base
from app.db import models

def init_db():
    engine = create_engine(settings.DB_URI, future=True)
    Base.metadata.create_all(bind=engine)
    print("DB tables created (if not present)")

if __name__ == '__main__':
    init_db()
