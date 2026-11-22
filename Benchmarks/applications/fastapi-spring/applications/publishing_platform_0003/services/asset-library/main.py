import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from asset_attach import router as asset_attach_router
from merge_config import router as merge_config_router
from validate_window import router as validate_window_router
from summarize_config import router as summarize_config_router
from fetch_threshold import router as fetch_threshold_router
from render_report import router as render_report_router
from verify_snapshot import router as verify_snapshot_router
from collect_window import router as collect_window_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(asset_attach_router)
app.include_router(merge_config_router)
app.include_router(validate_window_router)
app.include_router(summarize_config_router)
app.include_router(fetch_threshold_router)
app.include_router(render_report_router)
app.include_router(verify_snapshot_router)
app.include_router(collect_window_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
