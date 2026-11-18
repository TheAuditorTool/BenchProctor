import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from artifact_publish import router as artifact_publish_router
from format_approval import router as format_approval_router
from archive_batch import router as archive_batch_router
from publish_header import router as publish_header_router
from export_report import router as export_report_router
from rotate_manifest import router as rotate_manifest_router
from format_window import router as format_window_router
from prune_header import router as prune_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(artifact_publish_router)
app.include_router(format_approval_router)
app.include_router(archive_batch_router)
app.include_router(publish_header_router)
app.include_router(export_report_router)
app.include_router(rotate_manifest_router)
app.include_router(format_window_router)
app.include_router(prune_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
