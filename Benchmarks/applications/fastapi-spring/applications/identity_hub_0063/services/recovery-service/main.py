import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from recovery_start import router as recovery_start_router
from summarize_bundle import router as summarize_bundle_router
from merge_threshold import router as merge_threshold_router
from resolve_batch import router as resolve_batch_router
from reconcile_config import router as reconcile_config_router
from publish_config import router as publish_config_router
from render_report import router as render_report_router
from export_header import router as export_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(recovery_start_router)
app.include_router(summarize_bundle_router)
app.include_router(merge_threshold_router)
app.include_router(resolve_batch_router)
app.include_router(reconcile_config_router)
app.include_router(publish_config_router)
app.include_router(render_report_router)
app.include_router(export_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
