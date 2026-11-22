import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from payload_transform import router as payload_transform_router
from reconcile_ledger import router as reconcile_ledger_router
from compact_connector import router as compact_connector_router
from resolve_checkpoint import router as resolve_checkpoint_router
from archive_policy import router as archive_policy_router
from resolve_digest import router as resolve_digest_router
from format_record import router as format_record_router
from export_batch import router as export_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(payload_transform_router)
app.include_router(reconcile_ledger_router)
app.include_router(compact_connector_router)
app.include_router(resolve_checkpoint_router)
app.include_router(archive_policy_router)
app.include_router(resolve_digest_router)
app.include_router(format_record_router)
app.include_router(export_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
