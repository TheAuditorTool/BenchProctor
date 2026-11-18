import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from supplier_feed import router as supplier_feed_router
from export_record import router as export_record_router
from format_bundle import router as format_bundle_router
from export_snapshot import router as export_snapshot_router
from publish_checkpoint import router as publish_checkpoint_router
from publish_digest import router as publish_digest_router
from reconcile_batch import router as reconcile_batch_router
from compact_checkpoint import router as compact_checkpoint_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(supplier_feed_router)
app.include_router(export_record_router)
app.include_router(format_bundle_router)
app.include_router(export_snapshot_router)
app.include_router(publish_checkpoint_router)
app.include_router(publish_digest_router)
app.include_router(reconcile_batch_router)
app.include_router(compact_checkpoint_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
