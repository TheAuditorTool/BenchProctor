import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from stream_manifest import router as stream_manifest_router
from enrich_schedule import router as enrich_schedule_router
from load_caption import router as load_caption_router
from validate_bundle import router as validate_bundle_router
from prune_policy import router as prune_policy_router
from archive_record import router as archive_record_router
from merge_receipt import router as merge_receipt_router
from fetch_config import router as fetch_config_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(stream_manifest_router)
app.include_router(enrich_schedule_router)
app.include_router(load_caption_router)
app.include_router(validate_bundle_router)
app.include_router(prune_policy_router)
app.include_router(archive_record_router)
app.include_router(merge_receipt_router)
app.include_router(fetch_config_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
