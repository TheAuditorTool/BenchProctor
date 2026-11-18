import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from retention_sweep import router as retention_sweep_router
from rotate_checkpoint import router as rotate_checkpoint_router
from validate_checkpoint import router as validate_checkpoint_router
from compact_batch import router as compact_batch_router
from archive_schedule import router as archive_schedule_router
from annotate_header import router as annotate_header_router
from collect_report import router as collect_report_router
from fetch_threshold import router as fetch_threshold_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(retention_sweep_router)
app.include_router(rotate_checkpoint_router)
app.include_router(validate_checkpoint_router)
app.include_router(compact_batch_router)
app.include_router(archive_schedule_router)
app.include_router(annotate_header_router)
app.include_router(collect_report_router)
app.include_router(fetch_threshold_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
