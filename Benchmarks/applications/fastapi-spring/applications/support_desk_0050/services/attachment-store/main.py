import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from attachment_store import router as attachment_store_router
from enrich_header import router as enrich_header_router
from enrich_checkpoint import router as enrich_checkpoint_router
from publish_survey import router as publish_survey_router
from load_header import router as load_header_router
from audit_survey import router as audit_survey_router
from prune_record import router as prune_record_router
from render_escalation import router as render_escalation_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(attachment_store_router)
app.include_router(enrich_header_router)
app.include_router(enrich_checkpoint_router)
app.include_router(publish_survey_router)
app.include_router(load_header_router)
app.include_router(audit_survey_router)
app.include_router(prune_record_router)
app.include_router(render_escalation_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
