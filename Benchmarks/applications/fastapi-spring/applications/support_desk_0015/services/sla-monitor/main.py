import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from sla_check import router as sla_check_router
from prune_receipt import router as prune_receipt_router
from resolve_snapshot import router as resolve_snapshot_router
from summarize_config import router as summarize_config_router
from render_header import router as render_header_router
from prune_bundle import router as prune_bundle_router
from archive_escalation import router as archive_escalation_router
from prune_batch import router as prune_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(sla_check_router)
app.include_router(prune_receipt_router)
app.include_router(resolve_snapshot_router)
app.include_router(summarize_config_router)
app.include_router(render_header_router)
app.include_router(prune_bundle_router)
app.include_router(archive_escalation_router)
app.include_router(prune_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
