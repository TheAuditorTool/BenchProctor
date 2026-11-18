import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from metadata_index import router as metadata_index_router
from build_ledger import router as build_ledger_router
from enrich_window import router as enrich_window_router
from format_checkpoint import router as format_checkpoint_router
from reconcile_profile import router as reconcile_profile_router
from archive_header import router as archive_header_router
from load_report import router as load_report_router
from fetch_window import router as fetch_window_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(metadata_index_router)
app.include_router(build_ledger_router)
app.include_router(enrich_window_router)
app.include_router(format_checkpoint_router)
app.include_router(reconcile_profile_router)
app.include_router(archive_header_router)
app.include_router(load_report_router)
app.include_router(fetch_window_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
