import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from sla_check import router as sla_check_router
from audit_survey import router as audit_survey_router
from resolve_window import router as resolve_window_router
from validate_profile import router as validate_profile_router
from audit_policy import router as audit_policy_router
from summarize_roster import router as summarize_roster_router
from archive_bundle import router as archive_bundle_router
from rotate_macro import router as rotate_macro_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(sla_check_router)
app.include_router(audit_survey_router)
app.include_router(resolve_window_router)
app.include_router(validate_profile_router)
app.include_router(audit_policy_router)
app.include_router(summarize_roster_router)
app.include_router(archive_bundle_router)
app.include_router(rotate_macro_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
