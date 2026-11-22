import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from release_cut import router as release_cut_router
from publish_snapshot import router as publish_snapshot_router
from merge_window import router as merge_window_router
from build_summary import router as build_summary_router
from merge_canary import router as merge_canary_router
from normalize_config import router as normalize_config_router
from format_summary import router as format_summary_router
from export_report import router as export_report_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(release_cut_router)
app.include_router(publish_snapshot_router)
app.include_router(merge_window_router)
app.include_router(build_summary_router)
app.include_router(merge_canary_router)
app.include_router(normalize_config_router)
app.include_router(format_summary_router)
app.include_router(export_report_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
