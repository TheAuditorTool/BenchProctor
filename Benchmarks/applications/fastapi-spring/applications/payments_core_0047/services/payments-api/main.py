import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from payment_authorize import router as payment_authorize_router
from annotate_snapshot import router as annotate_snapshot_router
from audit_report import router as audit_report_router
from build_payout import router as build_payout_router
from fetch_record import router as fetch_record_router
from reconcile_dispute import router as reconcile_dispute_router
from fetch_profile import router as fetch_profile_router
from build_dispute import router as build_dispute_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(payment_authorize_router)
app.include_router(annotate_snapshot_router)
app.include_router(audit_report_router)
app.include_router(build_payout_router)
app.include_router(fetch_record_router)
app.include_router(reconcile_dispute_router)
app.include_router(fetch_profile_router)
app.include_router(build_dispute_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
