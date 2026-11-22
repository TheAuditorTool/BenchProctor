import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from archive_store import router as archive_store_router
from summarize_manifest import router as summarize_manifest_router
from format_redaction import router as format_redaction_router
from load_bundle import router as load_bundle_router
from resolve_bundle import router as resolve_bundle_router
from rotate_checkpoint import router as rotate_checkpoint_router
from archive_bundle import router as archive_bundle_router
from merge_ledger import router as merge_ledger_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(archive_store_router)
app.include_router(summarize_manifest_router)
app.include_router(format_redaction_router)
app.include_router(load_bundle_router)
app.include_router(resolve_bundle_router)
app.include_router(rotate_checkpoint_router)
app.include_router(archive_bundle_router)
app.include_router(merge_ledger_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
