import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from message_publish import router as message_publish_router
from annotate_manifest import router as annotate_manifest_router
from normalize_snapshot import router as normalize_snapshot_router
from render_report import router as render_report_router
from enrich_header import router as enrich_header_router
from format_checkpoint import router as format_checkpoint_router
from publish_schedule import router as publish_schedule_router
from summarize_schedule import router as summarize_schedule_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(message_publish_router)
app.include_router(annotate_manifest_router)
app.include_router(normalize_snapshot_router)
app.include_router(render_report_router)
app.include_router(enrich_header_router)
app.include_router(format_checkpoint_router)
app.include_router(publish_schedule_router)
app.include_router(summarize_schedule_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
