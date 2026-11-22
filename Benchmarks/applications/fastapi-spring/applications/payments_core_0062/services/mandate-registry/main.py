import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from mandate_register import router as mandate_register_router
from enrich_roster import router as enrich_roster_router
from verify_batch import router as verify_batch_router
from verify_roster import router as verify_roster_router
from merge_report import router as merge_report_router
from compact_config import router as compact_config_router
from merge_threshold import router as merge_threshold_router
from archive_snapshot import router as archive_snapshot_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(mandate_register_router)
app.include_router(enrich_roster_router)
app.include_router(verify_batch_router)
app.include_router(verify_roster_router)
app.include_router(merge_report_router)
app.include_router(compact_config_router)
app.include_router(merge_threshold_router)
app.include_router(archive_snapshot_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
