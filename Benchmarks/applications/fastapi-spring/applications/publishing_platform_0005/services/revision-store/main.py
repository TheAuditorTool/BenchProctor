import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from revision_save import router as revision_save_router
from rotate_snapshot import router as rotate_snapshot_router
from publish_manifest import router as publish_manifest_router
from audit_checkpoint import router as audit_checkpoint_router
from prune_roster import router as prune_roster_router
from rotate_summary import router as rotate_summary_router
from render_config import router as render_config_router
from merge_snapshot import router as merge_snapshot_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(revision_save_router)
app.include_router(rotate_snapshot_router)
app.include_router(publish_manifest_router)
app.include_router(audit_checkpoint_router)
app.include_router(prune_roster_router)
app.include_router(rotate_summary_router)
app.include_router(render_config_router)
app.include_router(merge_snapshot_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
