import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from cycle_count import router as cycle_count_router
from summarize_header import router as summarize_header_router
from audit_stock import router as audit_stock_router
from annotate_snapshot import router as annotate_snapshot_router
from annotate_schedule import router as annotate_schedule_router
from build_snapshot import router as build_snapshot_router
from enrich_ledger import router as enrich_ledger_router
from archive_ledger import router as archive_ledger_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(cycle_count_router)
app.include_router(summarize_header_router)
app.include_router(audit_stock_router)
app.include_router(annotate_snapshot_router)
app.include_router(annotate_schedule_router)
app.include_router(build_snapshot_router)
app.include_router(enrich_ledger_router)
app.include_router(archive_ledger_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
