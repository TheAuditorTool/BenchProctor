import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from log_ship import router as log_ship_router
from load_schedule import router as load_schedule_router
from resolve_window import router as resolve_window_router
from verify_index import router as verify_index_router
from normalize_alert import router as normalize_alert_router
from load_threshold import router as load_threshold_router
from rotate_policy import router as rotate_policy_router
from merge_summary import router as merge_summary_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(log_ship_router)
app.include_router(load_schedule_router)
app.include_router(resolve_window_router)
app.include_router(verify_index_router)
app.include_router(normalize_alert_router)
app.include_router(load_threshold_router)
app.include_router(rotate_policy_router)
app.include_router(merge_summary_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
