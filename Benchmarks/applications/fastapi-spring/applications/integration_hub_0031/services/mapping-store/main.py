import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from field_mapping import router as field_mapping_router
from summarize_header import router as summarize_header_router
from validate_mapping import router as validate_mapping_router
from summarize_threshold import router as summarize_threshold_router
from fetch_summary import router as fetch_summary_router
from collect_report import router as collect_report_router
from archive_webhook import router as archive_webhook_router
from summarize_webhook import router as summarize_webhook_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(field_mapping_router)
app.include_router(summarize_header_router)
app.include_router(validate_mapping_router)
app.include_router(summarize_threshold_router)
app.include_router(fetch_summary_router)
app.include_router(collect_report_router)
app.include_router(archive_webhook_router)
app.include_router(summarize_webhook_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
