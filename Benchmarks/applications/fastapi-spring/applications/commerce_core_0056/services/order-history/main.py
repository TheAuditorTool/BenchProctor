import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from order_lookup import router as order_lookup_router
from verify_window import router as verify_window_router
from archive_policy import router as archive_policy_router
from resolve_bundle import router as resolve_bundle_router
from enrich_report import router as enrich_report_router
from validate_threshold import router as validate_threshold_router
from compact_roster import router as compact_roster_router
from verify_order import router as verify_order_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(order_lookup_router)
app.include_router(verify_window_router)
app.include_router(archive_policy_router)
app.include_router(resolve_bundle_router)
app.include_router(enrich_report_router)
app.include_router(validate_threshold_router)
app.include_router(compact_roster_router)
app.include_router(verify_order_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
