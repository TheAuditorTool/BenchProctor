import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from device_enroll import router as device_enroll_router
from summarize_index import router as summarize_index_router
from annotate_profile import router as annotate_profile_router
from summarize_policy import router as summarize_policy_router
from export_summary import router as export_summary_router
from reconcile_summary import router as reconcile_summary_router
from render_snapshot import router as render_snapshot_router
from annotate_policy import router as annotate_policy_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(device_enroll_router)
app.include_router(summarize_index_router)
app.include_router(annotate_profile_router)
app.include_router(summarize_policy_router)
app.include_router(export_summary_router)
app.include_router(reconcile_summary_router)
app.include_router(render_snapshot_router)
app.include_router(annotate_policy_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
