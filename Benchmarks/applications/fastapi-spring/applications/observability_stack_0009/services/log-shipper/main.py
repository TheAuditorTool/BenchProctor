import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from log_ship import router as log_ship_router
from validate_receipt import router as validate_receipt_router
from validate_bundle import router as validate_bundle_router
from load_summary import router as load_summary_router
from compact_threshold import router as compact_threshold_router
from fetch_index import router as fetch_index_router
from enrich_record import router as enrich_record_router
from normalize_schedule import router as normalize_schedule_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(log_ship_router)
app.include_router(validate_receipt_router)
app.include_router(validate_bundle_router)
app.include_router(load_summary_router)
app.include_router(compact_threshold_router)
app.include_router(fetch_index_router)
app.include_router(enrich_record_router)
app.include_router(normalize_schedule_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
