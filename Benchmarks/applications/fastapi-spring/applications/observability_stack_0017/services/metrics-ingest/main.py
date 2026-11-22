import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from metric_ingest import router as metric_ingest_router
from archive_receipt import router as archive_receipt_router
from reconcile_sample import router as reconcile_sample_router
from normalize_policy import router as normalize_policy_router
from resolve_snapshot import router as resolve_snapshot_router
from load_record import router as load_record_router
from compact_config import router as compact_config_router
from render_policy import router as render_policy_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(metric_ingest_router)
app.include_router(archive_receipt_router)
app.include_router(reconcile_sample_router)
app.include_router(normalize_policy_router)
app.include_router(resolve_snapshot_router)
app.include_router(load_record_router)
app.include_router(compact_config_router)
app.include_router(render_policy_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
