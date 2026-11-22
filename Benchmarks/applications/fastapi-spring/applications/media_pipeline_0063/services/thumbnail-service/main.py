import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from thumbnail_render import router as thumbnail_render_router
from prune_manifest import router as prune_manifest_router
from enrich_threshold import router as enrich_threshold_router
from publish_config import router as publish_config_router
from annotate_schedule import router as annotate_schedule_router
from normalize_record import router as normalize_record_router
from enrich_snapshot import router as enrich_snapshot_router
from prune_record import router as prune_record_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(thumbnail_render_router)
app.include_router(prune_manifest_router)
app.include_router(enrich_threshold_router)
app.include_router(publish_config_router)
app.include_router(annotate_schedule_router)
app.include_router(normalize_record_router)
app.include_router(enrich_snapshot_router)
app.include_router(prune_record_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
