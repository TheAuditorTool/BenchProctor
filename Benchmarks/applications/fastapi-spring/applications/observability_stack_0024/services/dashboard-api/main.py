import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from dashboard_query import router as dashboard_query_router
from prune_ledger import router as prune_ledger_router
from resolve_header import router as resolve_header_router
from enrich_index import router as enrich_index_router
from collect_bundle import router as collect_bundle_router
from collect_report import router as collect_report_router
from annotate_record import router as annotate_record_router
from format_digest import router as format_digest_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(dashboard_query_router)
app.include_router(prune_ledger_router)
app.include_router(resolve_header_router)
app.include_router(enrich_index_router)
app.include_router(collect_bundle_router)
app.include_router(collect_report_router)
app.include_router(annotate_record_router)
app.include_router(format_digest_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
