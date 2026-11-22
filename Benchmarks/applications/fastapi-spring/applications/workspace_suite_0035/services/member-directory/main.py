import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from member_invite import router as member_invite_router
from annotate_summary import router as annotate_summary_router
from normalize_roster import router as normalize_roster_router
from rotate_profile import router as rotate_profile_router
from audit_membership import router as audit_membership_router
from annotate_policy import router as annotate_policy_router
from normalize_record import router as normalize_record_router
from collect_threshold import router as collect_threshold_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(member_invite_router)
app.include_router(annotate_summary_router)
app.include_router(normalize_roster_router)
app.include_router(rotate_profile_router)
app.include_router(audit_membership_router)
app.include_router(annotate_policy_router)
app.include_router(normalize_record_router)
app.include_router(collect_threshold_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
