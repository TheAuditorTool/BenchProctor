import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from recovery_start import router as recovery_start_router
from verify_batch import router as verify_batch_router
from audit_report import router as audit_report_router
from prune_policy import router as prune_policy_router
from audit_digest import router as audit_digest_router
from validate_manifest import router as validate_manifest_router
from summarize_schedule import router as summarize_schedule_router
from enrich_config import router as enrich_config_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(recovery_start_router)
app.include_router(verify_batch_router)
app.include_router(audit_report_router)
app.include_router(prune_policy_router)
app.include_router(audit_digest_router)
app.include_router(validate_manifest_router)
app.include_router(summarize_schedule_router)
app.include_router(enrich_config_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
