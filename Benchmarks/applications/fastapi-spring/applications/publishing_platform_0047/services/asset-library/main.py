import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from asset_attach import router as asset_attach_router
from reconcile_record import router as reconcile_record_router
from archive_schedule import router as archive_schedule_router
from export_config import router as export_config_router
from fetch_taxonomy import router as fetch_taxonomy_router
from compact_roster import router as compact_roster_router
from merge_header import router as merge_header_router
from compact_revision import router as compact_revision_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(asset_attach_router)
app.include_router(reconcile_record_router)
app.include_router(archive_schedule_router)
app.include_router(export_config_router)
app.include_router(fetch_taxonomy_router)
app.include_router(compact_roster_router)
app.include_router(merge_header_router)
app.include_router(compact_revision_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
