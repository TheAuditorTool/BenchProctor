import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from tracking_poll import router as tracking_poll_router
from build_record import router as build_record_router
from rotate_label import router as rotate_label_router
from compact_policy import router as compact_policy_router
from audit_batch import router as audit_batch_router
from collect_profile import router as collect_profile_router
from compact_threshold import router as compact_threshold_router
from archive_record import router as archive_record_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(tracking_poll_router)
app.include_router(build_record_router)
app.include_router(rotate_label_router)
app.include_router(compact_policy_router)
app.include_router(audit_batch_router)
app.include_router(collect_profile_router)
app.include_router(compact_threshold_router)
app.include_router(archive_record_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
