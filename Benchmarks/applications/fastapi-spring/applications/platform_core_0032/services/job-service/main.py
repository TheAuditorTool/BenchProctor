import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from job_schedule import router as job_schedule_router
from build_header import router as build_header_router
from publish_checkpoint import router as publish_checkpoint_router
from annotate_snapshot import router as annotate_snapshot_router
from collect_quota import router as collect_quota_router
from merge_profile import router as merge_profile_router
from merge_report import router as merge_report_router
from build_summary import router as build_summary_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(job_schedule_router)
app.include_router(build_header_router)
app.include_router(publish_checkpoint_router)
app.include_router(annotate_snapshot_router)
app.include_router(collect_quota_router)
app.include_router(merge_profile_router)
app.include_router(merge_report_router)
app.include_router(build_summary_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
