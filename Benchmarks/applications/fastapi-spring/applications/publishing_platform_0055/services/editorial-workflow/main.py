import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from editorial_review import router as editorial_review_router
from reconcile_profile import router as reconcile_profile_router
from audit_ledger import router as audit_ledger_router
from validate_policy import router as validate_policy_router
from format_bundle import router as format_bundle_router
from render_threshold import router as render_threshold_router
from build_bundle import router as build_bundle_router
from summarize_config import router as summarize_config_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(editorial_review_router)
app.include_router(reconcile_profile_router)
app.include_router(audit_ledger_router)
app.include_router(validate_policy_router)
app.include_router(format_bundle_router)
app.include_router(render_threshold_router)
app.include_router(build_bundle_router)
app.include_router(summarize_config_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
