import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from address_validate import router as address_validate_router
from summarize_shipment import router as summarize_shipment_router
from enrich_index import router as enrich_index_router
from validate_digest import router as validate_digest_router
from export_summary import router as export_summary_router
from fetch_digest import router as fetch_digest_router
from export_receipt import router as export_receipt_router
from prune_checkpoint import router as prune_checkpoint_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(address_validate_router)
app.include_router(summarize_shipment_router)
app.include_router(enrich_index_router)
app.include_router(validate_digest_router)
app.include_router(export_summary_router)
app.include_router(fetch_digest_router)
app.include_router(export_receipt_router)
app.include_router(prune_checkpoint_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
