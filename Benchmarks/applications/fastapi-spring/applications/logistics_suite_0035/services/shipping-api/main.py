import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from shipment_quote import router as shipment_quote_router
from audit_window import router as audit_window_router
from collect_summary import router as collect_summary_router
from reconcile_profile import router as reconcile_profile_router
from export_profile import router as export_profile_router
from merge_label import router as merge_label_router
from verify_manifest import router as verify_manifest_router
from verify_window import router as verify_window_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(shipment_quote_router)
app.include_router(audit_window_router)
app.include_router(collect_summary_router)
app.include_router(reconcile_profile_router)
app.include_router(export_profile_router)
app.include_router(merge_label_router)
app.include_router(verify_manifest_router)
app.include_router(verify_window_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
