import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from partner_register import router as partner_register_router
from export_digest import router as export_digest_router
from reconcile_snapshot import router as reconcile_snapshot_router
from render_snapshot import router as render_snapshot_router
from annotate_digest import router as annotate_digest_router
from enrich_threshold import router as enrich_threshold_router
from resolve_window import router as resolve_window_router
from verify_threshold import router as verify_threshold_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(partner_register_router)
app.include_router(export_digest_router)
app.include_router(reconcile_snapshot_router)
app.include_router(render_snapshot_router)
app.include_router(annotate_digest_router)
app.include_router(enrich_threshold_router)
app.include_router(resolve_window_router)
app.include_router(verify_threshold_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
