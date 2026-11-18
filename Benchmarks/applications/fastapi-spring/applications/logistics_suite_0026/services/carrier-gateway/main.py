import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from carrier_dispatch import router as carrier_dispatch_router
from summarize_snapshot import router as summarize_snapshot_router
from reconcile_manifest import router as reconcile_manifest_router
from resolve_record import router as resolve_record_router
from export_record import router as export_record_router
from archive_roster import router as archive_roster_router
from build_threshold import router as build_threshold_router
from audit_receipt import router as audit_receipt_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(carrier_dispatch_router)
app.include_router(summarize_snapshot_router)
app.include_router(reconcile_manifest_router)
app.include_router(resolve_record_router)
app.include_router(export_record_router)
app.include_router(archive_roster_router)
app.include_router(build_threshold_router)
app.include_router(audit_receipt_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
