import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from asset_upload import router as asset_upload_router
from build_snapshot import router as build_snapshot_router
from build_header import router as build_header_router
from reconcile_asset import router as reconcile_asset_router
from verify_receipt import router as verify_receipt_router
from enrich_receipt import router as enrich_receipt_router
from publish_profile import router as publish_profile_router
from prune_rendition import router as prune_rendition_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(asset_upload_router)
app.include_router(build_snapshot_router)
app.include_router(build_header_router)
app.include_router(reconcile_asset_router)
app.include_router(verify_receipt_router)
app.include_router(enrich_receipt_router)
app.include_router(publish_profile_router)
app.include_router(prune_rendition_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
