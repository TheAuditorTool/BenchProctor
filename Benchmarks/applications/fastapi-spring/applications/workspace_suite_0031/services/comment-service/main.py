import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from comment_post import router as comment_post_router
from reconcile_manifest import router as reconcile_manifest_router
from reconcile_comment import router as reconcile_comment_router
from compact_manifest import router as compact_manifest_router
from load_receipt import router as load_receipt_router
from annotate_ledger import router as annotate_ledger_router
from archive_snapshot import router as archive_snapshot_router
from format_record import router as format_record_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(comment_post_router)
app.include_router(reconcile_manifest_router)
app.include_router(reconcile_comment_router)
app.include_router(compact_manifest_router)
app.include_router(load_receipt_router)
app.include_router(annotate_ledger_router)
app.include_router(archive_snapshot_router)
app.include_router(format_record_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
