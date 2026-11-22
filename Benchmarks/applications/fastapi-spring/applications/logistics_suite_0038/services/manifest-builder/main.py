import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from manifest_build import router as manifest_build_router
from summarize_window import router as summarize_window_router
from fetch_checkpoint import router as fetch_checkpoint_router
from resolve_shipment import router as resolve_shipment_router
from archive_config import router as archive_config_router
from build_checkpoint import router as build_checkpoint_router
from build_batch import router as build_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(manifest_build_router)
app.include_router(summarize_window_router)
app.include_router(fetch_checkpoint_router)
app.include_router(resolve_shipment_router)
app.include_router(archive_config_router)
app.include_router(build_checkpoint_router)
app.include_router(build_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
