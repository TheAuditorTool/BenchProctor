import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from convert_job import router as convert_job_router
from annotate_bundle import router as annotate_bundle_router
from normalize_snapshot import router as normalize_snapshot_router
from rotate_receipt import router as rotate_receipt_router
from fetch_threshold import router as fetch_threshold_router
from build_checkpoint import router as build_checkpoint_router
from annotate_header import router as annotate_header_router
from reconcile_bundle import router as reconcile_bundle_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(convert_job_router)
app.include_router(annotate_bundle_router)
app.include_router(normalize_snapshot_router)
app.include_router(rotate_receipt_router)
app.include_router(fetch_threshold_router)
app.include_router(build_checkpoint_router)
app.include_router(annotate_header_router)
app.include_router(reconcile_bundle_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
