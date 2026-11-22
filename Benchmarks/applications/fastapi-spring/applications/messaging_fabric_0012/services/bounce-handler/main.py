import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from bounce_record import router as bounce_record_router
from verify_schedule import router as verify_schedule_router
from render_policy import router as render_policy_router
from archive_index import router as archive_index_router
from reconcile_batch import router as reconcile_batch_router
from enrich_header import router as enrich_header_router
from publish_checkpoint import router as publish_checkpoint_router
from audit_ledger import router as audit_ledger_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(bounce_record_router)
app.include_router(verify_schedule_router)
app.include_router(render_policy_router)
app.include_router(archive_index_router)
app.include_router(reconcile_batch_router)
app.include_router(enrich_header_router)
app.include_router(publish_checkpoint_router)
app.include_router(audit_ledger_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
