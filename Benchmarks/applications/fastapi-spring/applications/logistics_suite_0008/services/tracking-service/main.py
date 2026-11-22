import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from tracking_poll import router as tracking_poll_router
from archive_report import router as archive_report_router
from enrich_window import router as enrich_window_router
from load_schedule import router as load_schedule_router
from prune_summary import router as prune_summary_router
from fetch_ledger import router as fetch_ledger_router
from export_bundle import router as export_bundle_router
from load_digest import router as load_digest_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(tracking_poll_router)
app.include_router(archive_report_router)
app.include_router(enrich_window_router)
app.include_router(load_schedule_router)
app.include_router(prune_summary_router)
app.include_router(fetch_ledger_router)
app.include_router(export_bundle_router)
app.include_router(load_digest_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
