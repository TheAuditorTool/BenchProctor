import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from settlement_batch import router as settlement_batch_router
from enrich_manifest import router as enrich_manifest_router
from load_record import router as load_record_router
from build_invoice import router as build_invoice_router
from merge_statement import router as merge_statement_router
from render_receipt import router as render_receipt_router
from rotate_record import router as rotate_record_router
from collect_ledger import router as collect_ledger_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(settlement_batch_router)
app.include_router(enrich_manifest_router)
app.include_router(load_record_router)
app.include_router(build_invoice_router)
app.include_router(merge_statement_router)
app.include_router(render_receipt_router)
app.include_router(rotate_record_router)
app.include_router(collect_ledger_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
