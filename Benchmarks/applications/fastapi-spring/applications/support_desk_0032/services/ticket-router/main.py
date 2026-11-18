import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from ticket_route import router as ticket_route_router
from reconcile_checkpoint import router as reconcile_checkpoint_router
from prune_header import router as prune_header_router
from enrich_bundle import router as enrich_bundle_router
from resolve_survey import router as resolve_survey_router
from prune_snapshot import router as prune_snapshot_router
from validate_bundle import router as validate_bundle_router
from prune_receipt import router as prune_receipt_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(ticket_route_router)
app.include_router(reconcile_checkpoint_router)
app.include_router(prune_header_router)
app.include_router(enrich_bundle_router)
app.include_router(resolve_survey_router)
app.include_router(prune_snapshot_router)
app.include_router(validate_bundle_router)
app.include_router(prune_receipt_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
