import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from watermark_apply import router as watermark_apply_router
from annotate_receipt import router as annotate_receipt_router
from normalize_caption import router as normalize_caption_router
from compact_manifest import router as compact_manifest_router
from enrich_report import router as enrich_report_router
from archive_config import router as archive_config_router
from annotate_manifest import router as annotate_manifest_router
from publish_report import router as publish_report_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(watermark_apply_router)
app.include_router(annotate_receipt_router)
app.include_router(normalize_caption_router)
app.include_router(compact_manifest_router)
app.include_router(enrich_report_router)
app.include_router(archive_config_router)
app.include_router(annotate_manifest_router)
app.include_router(publish_report_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
