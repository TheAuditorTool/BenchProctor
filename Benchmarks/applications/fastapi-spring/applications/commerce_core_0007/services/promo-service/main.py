import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from promo_apply import router as promo_apply_router
from load_window import router as load_window_router
from collect_manifest import router as collect_manifest_router
from fetch_summary import router as fetch_summary_router
from render_report import router as render_report_router
from audit_ledger import router as audit_ledger_router
from publish_schedule import router as publish_schedule_router
from fetch_batch import router as fetch_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(promo_apply_router)
app.include_router(load_window_router)
app.include_router(collect_manifest_router)
app.include_router(fetch_summary_router)
app.include_router(render_report_router)
app.include_router(audit_ledger_router)
app.include_router(publish_schedule_router)
app.include_router(fetch_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
