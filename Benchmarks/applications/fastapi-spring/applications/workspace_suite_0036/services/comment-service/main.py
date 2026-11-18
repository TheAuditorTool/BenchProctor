import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from comment_post import router as comment_post_router
from rotate_schedule import router as rotate_schedule_router
from build_policy import router as build_policy_router
from normalize_document import router as normalize_document_router
from validate_bundle import router as validate_bundle_router
from summarize_record import router as summarize_record_router
from validate_workspace import router as validate_workspace_router
from prune_batch import router as prune_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(comment_post_router)
app.include_router(rotate_schedule_router)
app.include_router(build_policy_router)
app.include_router(normalize_document_router)
app.include_router(validate_bundle_router)
app.include_router(summarize_record_router)
app.include_router(validate_workspace_router)
app.include_router(prune_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
