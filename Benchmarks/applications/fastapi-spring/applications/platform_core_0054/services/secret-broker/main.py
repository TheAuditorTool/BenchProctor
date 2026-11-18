import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from secret_fetch import router as secret_fetch_router
from build_receipt import router as build_receipt_router
from rotate_summary import router as rotate_summary_router
from compact_secret import router as compact_secret_router
from rotate_config import router as rotate_config_router
from publish_secret import router as publish_secret_router
from reconcile_threshold import router as reconcile_threshold_router
from merge_record import router as merge_record_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(secret_fetch_router)
app.include_router(build_receipt_router)
app.include_router(rotate_summary_router)
app.include_router(compact_secret_router)
app.include_router(rotate_config_router)
app.include_router(publish_secret_router)
app.include_router(reconcile_threshold_router)
app.include_router(merge_record_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
