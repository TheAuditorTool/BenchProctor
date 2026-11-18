import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from sample_config import router as sample_config_router
from prune_digest import router as prune_digest_router
from compact_manifest import router as compact_manifest_router
from export_roster import router as export_roster_router
from verify_threshold import router as verify_threshold_router
from validate_record import router as validate_record_router
from prune_checkpoint import router as prune_checkpoint_router
from export_header import router as export_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(sample_config_router)
app.include_router(prune_digest_router)
app.include_router(compact_manifest_router)
app.include_router(export_roster_router)
app.include_router(verify_threshold_router)
app.include_router(validate_record_router)
app.include_router(prune_checkpoint_router)
app.include_router(export_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
