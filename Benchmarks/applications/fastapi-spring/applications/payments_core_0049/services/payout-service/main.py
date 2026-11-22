import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from payout_schedule import router as payout_schedule_router
from rotate_bundle import router as rotate_bundle_router
from merge_mandate import router as merge_mandate_router
from reconcile_schedule import router as reconcile_schedule_router
from summarize_digest import router as summarize_digest_router
from export_manifest import router as export_manifest_router
from publish_config import router as publish_config_router
from audit_bundle import router as audit_bundle_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(payout_schedule_router)
app.include_router(rotate_bundle_router)
app.include_router(merge_mandate_router)
app.include_router(reconcile_schedule_router)
app.include_router(summarize_digest_router)
app.include_router(export_manifest_router)
app.include_router(publish_config_router)
app.include_router(audit_bundle_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
