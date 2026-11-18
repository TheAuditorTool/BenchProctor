import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from settlement_batch import router as settlement_batch_router
from fetch_bundle import router as fetch_bundle_router
from archive_checkpoint import router as archive_checkpoint_router
from validate_statement import router as validate_statement_router
from summarize_report import router as summarize_report_router
from merge_config import router as merge_config_router
from archive_schedule import router as archive_schedule_router
from summarize_header import router as summarize_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(settlement_batch_router)
app.include_router(fetch_bundle_router)
app.include_router(archive_checkpoint_router)
app.include_router(validate_statement_router)
app.include_router(summarize_report_router)
app.include_router(merge_config_router)
app.include_router(archive_schedule_router)
app.include_router(summarize_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
