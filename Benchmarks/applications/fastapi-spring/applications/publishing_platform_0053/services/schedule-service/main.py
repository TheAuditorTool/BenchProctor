import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from publish_schedule import router as publish_schedule_router
from resolve_schedule import router as resolve_schedule_router
from normalize_checkpoint import router as normalize_checkpoint_router
from publish_report import router as publish_report_router
from normalize_policy import router as normalize_policy_router
from publish_snapshot import router as publish_snapshot_router
from fetch_receipt import router as fetch_receipt_router
from reconcile_article import router as reconcile_article_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(publish_schedule_router)
app.include_router(resolve_schedule_router)
app.include_router(normalize_checkpoint_router)
app.include_router(publish_report_router)
app.include_router(normalize_policy_router)
app.include_router(publish_snapshot_router)
app.include_router(fetch_receipt_router)
app.include_router(reconcile_article_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
