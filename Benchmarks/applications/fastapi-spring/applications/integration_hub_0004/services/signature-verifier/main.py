import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from signature_verify import router as signature_verify_router
from reconcile_summary import router as reconcile_summary_router
from summarize_ledger import router as summarize_ledger_router
from rotate_ledger import router as rotate_ledger_router
from validate_batch import router as validate_batch_router
from fetch_policy import router as fetch_policy_router
from enrich_report import router as enrich_report_router
from render_manifest import router as render_manifest_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(signature_verify_router)
app.include_router(reconcile_summary_router)
app.include_router(summarize_ledger_router)
app.include_router(rotate_ledger_router)
app.include_router(validate_batch_router)
app.include_router(fetch_policy_router)
app.include_router(enrich_report_router)
app.include_router(render_manifest_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
