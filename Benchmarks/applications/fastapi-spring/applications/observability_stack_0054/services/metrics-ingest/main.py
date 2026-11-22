import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from metric_ingest import router as metric_ingest_router
from validate_alert import router as validate_alert_router
from enrich_report import router as enrich_report_router
from build_threshold import router as build_threshold_router
from archive_index import router as archive_index_router
from resolve_bundle import router as resolve_bundle_router
from render_checkpoint import router as render_checkpoint_router
from rotate_threshold import router as rotate_threshold_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(metric_ingest_router)
app.include_router(validate_alert_router)
app.include_router(enrich_report_router)
app.include_router(build_threshold_router)
app.include_router(archive_index_router)
app.include_router(resolve_bundle_router)
app.include_router(render_checkpoint_router)
app.include_router(rotate_threshold_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
