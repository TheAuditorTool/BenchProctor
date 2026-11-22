import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from capture_settle import router as capture_settle_router
from compact_header import router as compact_header_router
from rotate_threshold import router as rotate_threshold_router
from publish_receipt import router as publish_receipt_router
from rotate_config import router as rotate_config_router
from merge_index import router as merge_index_router
from audit_checkpoint import router as audit_checkpoint_router
from merge_digest import router as merge_digest_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(capture_settle_router)
app.include_router(compact_header_router)
app.include_router(rotate_threshold_router)
app.include_router(publish_receipt_router)
app.include_router(rotate_config_router)
app.include_router(merge_index_router)
app.include_router(audit_checkpoint_router)
app.include_router(merge_digest_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
