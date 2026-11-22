import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from trace_collect import router as trace_collect_router
from fetch_report import router as fetch_report_router
from prune_digest import router as prune_digest_router
from compact_schedule import router as compact_schedule_router
from format_profile import router as format_profile_router
from collect_metric import router as collect_metric_router
from prune_profile import router as prune_profile_router
from summarize_roster import router as summarize_roster_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(trace_collect_router)
app.include_router(fetch_report_router)
app.include_router(prune_digest_router)
app.include_router(compact_schedule_router)
app.include_router(format_profile_router)
app.include_router(collect_metric_router)
app.include_router(prune_profile_router)
app.include_router(summarize_roster_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
