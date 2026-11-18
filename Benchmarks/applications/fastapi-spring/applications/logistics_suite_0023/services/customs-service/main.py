import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from customs_declare import router as customs_declare_router
from fetch_config import router as fetch_config_router
from compact_bundle import router as compact_bundle_router
from audit_digest import router as audit_digest_router
from prune_manifest import router as prune_manifest_router
from rotate_threshold import router as rotate_threshold_router
from fetch_carrier import router as fetch_carrier_router
from annotate_header import router as annotate_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(customs_declare_router)
app.include_router(fetch_config_router)
app.include_router(compact_bundle_router)
app.include_router(audit_digest_router)
app.include_router(prune_manifest_router)
app.include_router(rotate_threshold_router)
app.include_router(fetch_carrier_router)
app.include_router(annotate_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
