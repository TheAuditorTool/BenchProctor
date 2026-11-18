import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from payout_schedule import router as payout_schedule_router
from collect_report import router as collect_report_router
from compact_index import router as compact_index_router
from enrich_digest import router as enrich_digest_router
from render_batch import router as render_batch_router
from normalize_snapshot import router as normalize_snapshot_router
from format_manifest import router as format_manifest_router
from build_index import router as build_index_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(payout_schedule_router)
app.include_router(collect_report_router)
app.include_router(compact_index_router)
app.include_router(enrich_digest_router)
app.include_router(render_batch_router)
app.include_router(normalize_snapshot_router)
app.include_router(format_manifest_router)
app.include_router(build_index_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
