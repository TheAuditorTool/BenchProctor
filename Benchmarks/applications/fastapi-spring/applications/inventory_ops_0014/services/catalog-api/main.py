import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from sku_lookup import router as sku_lookup_router
from archive_header import router as archive_header_router
from enrich_header import router as enrich_header_router
from load_batch import router as load_batch_router
from render_ledger import router as render_ledger_router
from resolve_allocation import router as resolve_allocation_router
from rotate_digest import router as rotate_digest_router
from reconcile_summary import router as reconcile_summary_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(sku_lookup_router)
app.include_router(archive_header_router)
app.include_router(enrich_header_router)
app.include_router(load_batch_router)
app.include_router(render_ledger_router)
app.include_router(resolve_allocation_router)
app.include_router(rotate_digest_router)
app.include_router(reconcile_summary_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
