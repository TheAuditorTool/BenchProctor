import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from artifact_publish import router as artifact_publish_router
from verify_header import router as verify_header_router
from load_summary import router as load_summary_router
from prune_window import router as prune_window_router
from verify_report import router as verify_report_router
from publish_record import router as publish_record_router
from build_receipt import router as build_receipt_router
from rotate_policy import router as rotate_policy_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(artifact_publish_router)
app.include_router(verify_header_router)
app.include_router(load_summary_router)
app.include_router(prune_window_router)
app.include_router(verify_report_router)
app.include_router(publish_record_router)
app.include_router(build_receipt_router)
app.include_router(rotate_policy_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
