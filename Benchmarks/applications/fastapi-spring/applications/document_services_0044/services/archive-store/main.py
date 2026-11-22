import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from archive_store import router as archive_store_router
from summarize_config import router as summarize_config_router
from compact_index import router as compact_index_router
from archive_schedule import router as archive_schedule_router
from format_redaction import router as format_redaction_router
from archive_bundle import router as archive_bundle_router
from verify_policy import router as verify_policy_router
from reconcile_policy import router as reconcile_policy_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(archive_store_router)
app.include_router(summarize_config_router)
app.include_router(compact_index_router)
app.include_router(archive_schedule_router)
app.include_router(format_redaction_router)
app.include_router(archive_bundle_router)
app.include_router(verify_policy_router)
app.include_router(reconcile_policy_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
