import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from carrier_dispatch import router as carrier_dispatch_router
from render_roster import router as render_roster_router
from format_receipt import router as format_receipt_router
from rotate_waybill import router as rotate_waybill_router
from prune_summary import router as prune_summary_router
from publish_policy import router as publish_policy_router
from verify_bundle import router as verify_bundle_router
from validate_summary import router as validate_summary_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(carrier_dispatch_router)
app.include_router(render_roster_router)
app.include_router(format_receipt_router)
app.include_router(rotate_waybill_router)
app.include_router(prune_summary_router)
app.include_router(publish_policy_router)
app.include_router(verify_bundle_router)
app.include_router(validate_summary_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
