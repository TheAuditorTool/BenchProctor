import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from customs_declare import router as customs_declare_router
from render_summary import router as render_summary_router
from prune_schedule import router as prune_schedule_router
from audit_config import router as audit_config_router
from annotate_header import router as annotate_header_router
from export_checkpoint import router as export_checkpoint_router
from merge_checkpoint import router as merge_checkpoint_router
from build_waybill import router as build_waybill_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(customs_declare_router)
app.include_router(render_summary_router)
app.include_router(prune_schedule_router)
app.include_router(audit_config_router)
app.include_router(annotate_header_router)
app.include_router(export_checkpoint_router)
app.include_router(merge_checkpoint_router)
app.include_router(build_waybill_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
