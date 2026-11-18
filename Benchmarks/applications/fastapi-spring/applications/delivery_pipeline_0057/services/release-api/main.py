import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from release_cut import router as release_cut_router
from build_policy import router as build_policy_router
from archive_report import router as archive_report_router
from collect_digest import router as collect_digest_router
from reconcile_schedule import router as reconcile_schedule_router
from summarize_receipt import router as summarize_receipt_router
from export_checkpoint import router as export_checkpoint_router
from resolve_release import router as resolve_release_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(release_cut_router)
app.include_router(build_policy_router)
app.include_router(archive_report_router)
app.include_router(collect_digest_router)
app.include_router(reconcile_schedule_router)
app.include_router(summarize_receipt_router)
app.include_router(export_checkpoint_router)
app.include_router(resolve_release_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
