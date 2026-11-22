import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from ledger_post import router as ledger_post_router
from merge_report import router as merge_report_router
from rotate_ledger import router as rotate_ledger_router
from prune_summary import router as prune_summary_router
from normalize_invoice import router as normalize_invoice_router
from enrich_manifest import router as enrich_manifest_router
from validate_summary import router as validate_summary_router
from collect_header import router as collect_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(ledger_post_router)
app.include_router(merge_report_router)
app.include_router(rotate_ledger_router)
app.include_router(prune_summary_router)
app.include_router(normalize_invoice_router)
app.include_router(enrich_manifest_router)
app.include_router(validate_summary_router)
app.include_router(collect_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
