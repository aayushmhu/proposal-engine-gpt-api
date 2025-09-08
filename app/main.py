from fastapi import FastAPI
from app.api.v1 import routes_process, routes_edit, routes_history, routes_feedback
from app.core.logging import setup_logging
from app.db.base import  Base
from app.db.session import engine

setup_logging()

app = FastAPI(title="Proposal Processing Engine", version="0.1.0")

app.include_router(routes_process.router, prefix="/v1", tags=["process"])
app.include_router(routes_edit.router, prefix="/v1", tags=["edit"])
app.include_router(routes_history.router, prefix="/v1", tags=["history"])
app.include_router(routes_feedback.router, prefix="/v1", tags=["feedback"])

@app.get("/")
def root():
    return {"status": "ok", "service": "proposal-engine"}


Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)
