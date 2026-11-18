import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from config_rollout import router as config_rollout_router
from archive_roster import router as archive_roster_router
from render_quota import router as render_quota_router
from merge_policy import router as merge_policy_router
from archive_config import router as archive_config_router
from rotate_bundle import router as rotate_bundle_router
from audit_header import router as audit_header_router
from verify_receipt import router as verify_receipt_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(config_rollout_router)
app.include_router(archive_roster_router)
app.include_router(render_quota_router)
app.include_router(merge_policy_router)
app.include_router(archive_config_router)
app.include_router(rotate_bundle_router)
app.include_router(audit_header_router)
app.include_router(verify_receipt_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
