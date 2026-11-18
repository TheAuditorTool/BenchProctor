import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from job_schedule import router as job_schedule_router
from annotate_quota import router as annotate_quota_router
from build_batch import router as build_batch_router
from compact_batch import router as compact_batch_router
from summarize_profile import router as summarize_profile_router
from annotate_schedule import router as annotate_schedule_router
from build_index import router as build_index_router
from merge_snapshot import router as merge_snapshot_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(job_schedule_router)
app.include_router(annotate_quota_router)
app.include_router(build_batch_router)
app.include_router(compact_batch_router)
app.include_router(summarize_profile_router)
app.include_router(annotate_schedule_router)
app.include_router(build_index_router)
app.include_router(merge_snapshot_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
