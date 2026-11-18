import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from audit_append import router as audit_append_router
from export_roster import router as export_roster_router
from compact_header import router as compact_header_router
from annotate_schedule import router as annotate_schedule_router
from collect_digest import router as collect_digest_router
from build_config import router as build_config_router
from prune_record import router as prune_record_router
from audit_manifest import router as audit_manifest_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(audit_append_router)
app.include_router(export_roster_router)
app.include_router(compact_header_router)
app.include_router(annotate_schedule_router)
app.include_router(collect_digest_router)
app.include_router(build_config_router)
app.include_router(prune_record_router)
app.include_router(audit_manifest_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
