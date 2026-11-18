import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from member_invite import router as member_invite_router
from resolve_threshold import router as resolve_threshold_router
from audit_index import router as audit_index_router
from audit_roster import router as audit_roster_router
from export_config import router as export_config_router
from render_summary import router as render_summary_router
from normalize_snapshot import router as normalize_snapshot_router
from audit_checkpoint import router as audit_checkpoint_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(member_invite_router)
app.include_router(resolve_threshold_router)
app.include_router(audit_index_router)
app.include_router(audit_roster_router)
app.include_router(export_config_router)
app.include_router(render_summary_router)
app.include_router(normalize_snapshot_router)
app.include_router(audit_checkpoint_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
