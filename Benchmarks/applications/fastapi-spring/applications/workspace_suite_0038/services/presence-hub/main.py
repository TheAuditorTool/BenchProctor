import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from presence_track import router as presence_track_router
from compact_summary import router as compact_summary_router
from normalize_snapshot import router as normalize_snapshot_router
from publish_schedule import router as publish_schedule_router
from publish_config import router as publish_config_router
from render_checkpoint import router as render_checkpoint_router
from merge_header import router as merge_header_router
from build_document import router as build_document_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(presence_track_router)
app.include_router(compact_summary_router)
app.include_router(normalize_snapshot_router)
app.include_router(publish_schedule_router)
app.include_router(publish_config_router)
app.include_router(render_checkpoint_router)
app.include_router(merge_header_router)
app.include_router(build_document_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
