import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from revision_save import router as revision_save_router
from merge_receipt import router as merge_receipt_router
from resolve_manifest import router as resolve_manifest_router
from enrich_article import router as enrich_article_router
from compact_snapshot import router as compact_snapshot_router
from resolve_header import router as resolve_header_router
from render_record import router as render_record_router
from prune_revision import router as prune_revision_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(revision_save_router)
app.include_router(merge_receipt_router)
app.include_router(resolve_manifest_router)
app.include_router(enrich_article_router)
app.include_router(compact_snapshot_router)
app.include_router(resolve_header_router)
app.include_router(render_record_router)
app.include_router(prune_revision_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
