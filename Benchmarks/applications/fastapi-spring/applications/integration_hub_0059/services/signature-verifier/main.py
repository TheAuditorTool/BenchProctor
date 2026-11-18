import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from signature_verify import router as signature_verify_router
from reconcile_webhook import router as reconcile_webhook_router
from validate_profile import router as validate_profile_router
from enrich_mapping import router as enrich_mapping_router
from collect_manifest import router as collect_manifest_router
from collect_checkpoint import router as collect_checkpoint_router
from audit_roster import router as audit_roster_router
from export_digest import router as export_digest_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(signature_verify_router)
app.include_router(reconcile_webhook_router)
app.include_router(validate_profile_router)
app.include_router(enrich_mapping_router)
app.include_router(collect_manifest_router)
app.include_router(collect_checkpoint_router)
app.include_router(audit_roster_router)
app.include_router(export_digest_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
