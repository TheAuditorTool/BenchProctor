import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from payload_transform import router as payload_transform_router
from annotate_snapshot import router as annotate_snapshot_router
from normalize_ledger import router as normalize_ledger_router
from load_mapping import router as load_mapping_router
from rotate_checkpoint import router as rotate_checkpoint_router
from publish_mapping import router as publish_mapping_router
from build_webhook import router as build_webhook_router
from compact_checkpoint import router as compact_checkpoint_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(payload_transform_router)
app.include_router(annotate_snapshot_router)
app.include_router(normalize_ledger_router)
app.include_router(load_mapping_router)
app.include_router(rotate_checkpoint_router)
app.include_router(publish_mapping_router)
app.include_router(build_webhook_router)
app.include_router(compact_checkpoint_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
