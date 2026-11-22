import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from escalation_raise import router as escalation_raise_router
from resolve_config import router as resolve_config_router
from prune_report import router as prune_report_router
from normalize_profile import router as normalize_profile_router
from reconcile_index import router as reconcile_index_router
from resolve_index import router as resolve_index_router
from audit_bundle import router as audit_bundle_router
from enrich_config import router as enrich_config_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(escalation_raise_router)
app.include_router(resolve_config_router)
app.include_router(prune_report_router)
app.include_router(normalize_profile_router)
app.include_router(reconcile_index_router)
app.include_router(resolve_index_router)
app.include_router(audit_bundle_router)
app.include_router(enrich_config_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
