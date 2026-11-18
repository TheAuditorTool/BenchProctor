import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from anomaly_score import router as anomaly_score_router
from render_checkpoint import router as render_checkpoint_router
from build_bundle import router as build_bundle_router
from validate_bundle import router as validate_bundle_router
from resolve_bundle import router as resolve_bundle_router
from enrich_config import router as enrich_config_router
from merge_digest import router as merge_digest_router
from resolve_report import router as resolve_report_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(anomaly_score_router)
app.include_router(render_checkpoint_router)
app.include_router(build_bundle_router)
app.include_router(validate_bundle_router)
app.include_router(resolve_bundle_router)
app.include_router(enrich_config_router)
app.include_router(merge_digest_router)
app.include_router(resolve_report_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
