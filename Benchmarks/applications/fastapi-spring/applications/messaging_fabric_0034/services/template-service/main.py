import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from template_compose import router as template_compose_router
from compact_schedule import router as compact_schedule_router
from summarize_snapshot import router as summarize_snapshot_router
from resolve_manifest import router as resolve_manifest_router
from archive_summary import router as archive_summary_router
from audit_summary import router as audit_summary_router
from verify_bundle import router as verify_bundle_router
from compact_index import router as compact_index_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(template_compose_router)
app.include_router(compact_schedule_router)
app.include_router(summarize_snapshot_router)
app.include_router(resolve_manifest_router)
app.include_router(archive_summary_router)
app.include_router(audit_summary_router)
app.include_router(verify_bundle_router)
app.include_router(compact_index_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
