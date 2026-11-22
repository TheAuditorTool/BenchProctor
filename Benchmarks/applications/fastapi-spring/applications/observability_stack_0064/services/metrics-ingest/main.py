import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from metric_ingest import router as metric_ingest_router
from audit_schedule import router as audit_schedule_router
from prune_batch import router as prune_batch_router
from export_alert import router as export_alert_router
from render_manifest import router as render_manifest_router
from format_schedule import router as format_schedule_router
from annotate_digest import router as annotate_digest_router
from export_schedule import router as export_schedule_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(metric_ingest_router)
app.include_router(audit_schedule_router)
app.include_router(prune_batch_router)
app.include_router(export_alert_router)
app.include_router(render_manifest_router)
app.include_router(format_schedule_router)
app.include_router(annotate_digest_router)
app.include_router(export_schedule_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
