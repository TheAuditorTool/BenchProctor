import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from sample_config import router as sample_config_router
from fetch_config import router as fetch_config_router
from annotate_report import router as annotate_report_router
from compact_index import router as compact_index_router
from reconcile_threshold import router as reconcile_threshold_router
from enrich_schedule import router as enrich_schedule_router
from render_bundle import router as render_bundle_router
from collect_sample import router as collect_sample_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(sample_config_router)
app.include_router(fetch_config_router)
app.include_router(annotate_report_router)
app.include_router(compact_index_router)
app.include_router(reconcile_threshold_router)
app.include_router(enrich_schedule_router)
app.include_router(render_bundle_router)
app.include_router(collect_sample_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
