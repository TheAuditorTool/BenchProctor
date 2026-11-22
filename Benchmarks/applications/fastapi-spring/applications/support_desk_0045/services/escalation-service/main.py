import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from escalation_raise import router as escalation_raise_router
from load_bundle import router as load_bundle_router
from audit_manifest import router as audit_manifest_router
from annotate_summary import router as annotate_summary_router
from prune_summary import router as prune_summary_router
from enrich_ticket import router as enrich_ticket_router
from resolve_ticket import router as resolve_ticket_router
from reconcile_ticket import router as reconcile_ticket_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(escalation_raise_router)
app.include_router(load_bundle_router)
app.include_router(audit_manifest_router)
app.include_router(annotate_summary_router)
app.include_router(prune_summary_router)
app.include_router(enrich_ticket_router)
app.include_router(resolve_ticket_router)
app.include_router(reconcile_ticket_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
