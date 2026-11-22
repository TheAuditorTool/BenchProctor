import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from signature_verify import router as signature_verify_router
from archive_webhook import router as archive_webhook_router
from publish_window import router as publish_window_router
from audit_partner import router as audit_partner_router
from audit_batch import router as audit_batch_router
from validate_checkpoint import router as validate_checkpoint_router
from summarize_checkpoint import router as summarize_checkpoint_router
from reconcile_record import router as reconcile_record_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(signature_verify_router)
app.include_router(archive_webhook_router)
app.include_router(publish_window_router)
app.include_router(audit_partner_router)
app.include_router(audit_batch_router)
app.include_router(validate_checkpoint_router)
app.include_router(summarize_checkpoint_router)
app.include_router(reconcile_record_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
