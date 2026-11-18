import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from template_fill import router as template_fill_router
from verify_roster import router as verify_roster_router
from audit_record import router as audit_record_router
from compact_ledger import router as compact_ledger_router
from verify_bundle import router as verify_bundle_router
from resolve_profile import router as resolve_profile_router
from archive_batch import router as archive_batch_router
from annotate_config import router as annotate_config_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(template_fill_router)
app.include_router(verify_roster_router)
app.include_router(audit_record_router)
app.include_router(compact_ledger_router)
app.include_router(verify_bundle_router)
app.include_router(resolve_profile_router)
app.include_router(archive_batch_router)
app.include_router(annotate_config_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
