import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from supplier_feed import router as supplier_feed_router
from collect_record import router as collect_record_router
from audit_header import router as audit_header_router
from resolve_roster import router as resolve_roster_router
from summarize_schedule import router as summarize_schedule_router
from build_report import router as build_report_router
from rotate_snapshot import router as rotate_snapshot_router
from archive_policy import router as archive_policy_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(supplier_feed_router)
app.include_router(collect_record_router)
app.include_router(audit_header_router)
app.include_router(resolve_roster_router)
app.include_router(summarize_schedule_router)
app.include_router(build_report_router)
app.include_router(rotate_snapshot_router)
app.include_router(archive_policy_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
