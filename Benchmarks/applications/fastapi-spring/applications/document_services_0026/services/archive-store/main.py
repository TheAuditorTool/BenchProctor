import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from archive_store import router as archive_store_router
from audit_index import router as audit_index_router
from archive_digest import router as archive_digest_router
from publish_manifest import router as publish_manifest_router
from build_profile import router as build_profile_router
from validate_checkpoint import router as validate_checkpoint_router
from reconcile_checkpoint import router as reconcile_checkpoint_router
from resolve_roster import router as resolve_roster_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(archive_store_router)
app.include_router(audit_index_router)
app.include_router(archive_digest_router)
app.include_router(publish_manifest_router)
app.include_router(build_profile_router)
app.include_router(validate_checkpoint_router)
app.include_router(reconcile_checkpoint_router)
app.include_router(resolve_roster_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
