import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from statement_build import router as statement_build_router
from reconcile_window import router as reconcile_window_router
from summarize_summary import router as summarize_summary_router
from validate_checkpoint import router as validate_checkpoint_router
from resolve_header import router as resolve_header_router
from validate_schedule import router as validate_schedule_router
from validate_window import router as validate_window_router
from merge_summary import router as merge_summary_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(statement_build_router)
app.include_router(reconcile_window_router)
app.include_router(summarize_summary_router)
app.include_router(validate_checkpoint_router)
app.include_router(resolve_header_router)
app.include_router(validate_schedule_router)
app.include_router(validate_window_router)
app.include_router(merge_summary_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
