import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from fulfillment_queue import router as fulfillment_queue_router
from normalize_promotion import router as normalize_promotion_router
from compact_summary import router as compact_summary_router
from verify_policy import router as verify_policy_router
from format_cart import router as format_cart_router
from compact_config import router as compact_config_router
from export_report import router as export_report_router
from validate_manifest import router as validate_manifest_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(fulfillment_queue_router)
app.include_router(normalize_promotion_router)
app.include_router(compact_summary_router)
app.include_router(verify_policy_router)
app.include_router(format_cart_router)
app.include_router(compact_config_router)
app.include_router(export_report_router)
app.include_router(validate_manifest_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
