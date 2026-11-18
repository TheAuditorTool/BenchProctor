import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from thumbnail_render import router as thumbnail_render_router
from collect_manifest import router as collect_manifest_router
from collect_config import router as collect_config_router
from normalize_report import router as normalize_report_router
from enrich_report import router as enrich_report_router
from render_snapshot import router as render_snapshot_router
from load_ledger import router as load_ledger_router
from prune_snapshot import router as prune_snapshot_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(thumbnail_render_router)
app.include_router(collect_manifest_router)
app.include_router(collect_config_router)
app.include_router(normalize_report_router)
app.include_router(enrich_report_router)
app.include_router(render_snapshot_router)
app.include_router(load_ledger_router)
app.include_router(prune_snapshot_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
