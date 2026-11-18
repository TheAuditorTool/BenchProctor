import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from consent_record import router as consent_record_router
from annotate_index import router as annotate_index_router
from validate_device import router as validate_device_router
from normalize_snapshot import router as normalize_snapshot_router
from render_summary import router as render_summary_router
from summarize_device import router as summarize_device_router
from audit_threshold import router as audit_threshold_router
from verify_device import router as verify_device_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(consent_record_router)
app.include_router(annotate_index_router)
app.include_router(validate_device_router)
app.include_router(normalize_snapshot_router)
app.include_router(render_summary_router)
app.include_router(summarize_device_router)
app.include_router(audit_threshold_router)
app.include_router(verify_device_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
