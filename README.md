# Proposal Processing Engine (FastAPI)


## Quickstart (local, SQLite)
1. Create and activate a virtualenv
2. pip install -r requirements.txt
3. cp .env.example .env and edit if needed
4. python -m spacy download en_core_web_sm
5. alembic is included but for quick test the models will auto-create with SQLite.
6. Run: `python app/main.py`

Endpoints:
- POST /v1/process  -> Process a document (minimal NLP + GPT wrapper)
- GET / -> health


### Setup
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Activate Virtual Env
source .venv/bin/activate

### Run
uvicorn app.main:app --reload --port 8080


### View API Docs
http://127.0.0.1:8080/docs