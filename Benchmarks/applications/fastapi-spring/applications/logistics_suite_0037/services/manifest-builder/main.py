import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from manifest_build import router as manifest_build_router
from rotate_window import router as rotate_window_router
from validate_summary import router as validate_summary_router
from prune_label import router as prune_label_router
from archive_snapshot import router as archive_snapshot_router
from annotate_roster import router as annotate_roster_router
from prune_config import router as prune_config_router
from compact_waybill import router as compact_waybill_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(manifest_build_router)
app.include_router(rotate_window_router)
app.include_router(validate_summary_router)
app.include_router(prune_label_router)
app.include_router(archive_snapshot_router)
app.include_router(annotate_roster_router)
app.include_router(prune_config_router)
app.include_router(compact_waybill_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
