import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from macro_apply import router as macro_apply_router
from publish_escalation import router as publish_escalation_router
from normalize_digest import router as normalize_digest_router
from fetch_roster import router as fetch_roster_router
from normalize_snapshot import router as normalize_snapshot_router
from build_receipt import router as build_receipt_router
from export_report import router as export_report_router
from render_threshold import router as render_threshold_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(macro_apply_router)
app.include_router(publish_escalation_router)
app.include_router(normalize_digest_router)
app.include_router(fetch_roster_router)
app.include_router(normalize_snapshot_router)
app.include_router(build_receipt_router)
app.include_router(export_report_router)
app.include_router(render_threshold_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
