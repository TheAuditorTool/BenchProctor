import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from trace_collect import router as trace_collect_router
from reconcile_snapshot import router as reconcile_snapshot_router
from rotate_bundle import router as rotate_bundle_router
from render_report import router as render_report_router
from enrich_trace import router as enrich_trace_router
from reconcile_roster import router as reconcile_roster_router
from export_window import router as export_window_router
from reconcile_batch import router as reconcile_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(trace_collect_router)
app.include_router(reconcile_snapshot_router)
app.include_router(rotate_bundle_router)
app.include_router(render_report_router)
app.include_router(enrich_trace_router)
app.include_router(reconcile_roster_router)
app.include_router(export_window_router)
app.include_router(reconcile_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
