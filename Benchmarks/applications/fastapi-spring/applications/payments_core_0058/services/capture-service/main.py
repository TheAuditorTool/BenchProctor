import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from capture_settle import router as capture_settle_router
from format_report import router as format_report_router
from collect_header import router as collect_header_router
from annotate_manifest import router as annotate_manifest_router
from fetch_profile import router as fetch_profile_router
from reconcile_summary import router as reconcile_summary_router
from summarize_profile import router as summarize_profile_router
from build_header import router as build_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(capture_settle_router)
app.include_router(format_report_router)
app.include_router(collect_header_router)
app.include_router(annotate_manifest_router)
app.include_router(fetch_profile_router)
app.include_router(reconcile_summary_router)
app.include_router(summarize_profile_router)
app.include_router(build_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
