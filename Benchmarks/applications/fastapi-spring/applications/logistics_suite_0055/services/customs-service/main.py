import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from customs_declare import router as customs_declare_router
from audit_report import router as audit_report_router
from reconcile_checkpoint import router as reconcile_checkpoint_router
from archive_digest import router as archive_digest_router
from publish_window import router as publish_window_router
from publish_schedule import router as publish_schedule_router
from publish_waybill import router as publish_waybill_router
from summarize_ledger import router as summarize_ledger_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(customs_declare_router)
app.include_router(audit_report_router)
app.include_router(reconcile_checkpoint_router)
app.include_router(archive_digest_router)
app.include_router(publish_window_router)
app.include_router(publish_schedule_router)
app.include_router(publish_waybill_router)
app.include_router(summarize_ledger_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
