import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from case_open import router as case_open_router
from summarize_config import router as summarize_config_router
from rotate_profile import router as rotate_profile_router
from audit_window import router as audit_window_router
from reconcile_record import router as reconcile_record_router
from enrich_schedule import router as enrich_schedule_router
from validate_manifest import router as validate_manifest_router
from verify_index import router as verify_index_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(case_open_router)
app.include_router(summarize_config_router)
app.include_router(rotate_profile_router)
app.include_router(audit_window_router)
app.include_router(reconcile_record_router)
app.include_router(enrich_schedule_router)
app.include_router(validate_manifest_router)
app.include_router(verify_index_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
