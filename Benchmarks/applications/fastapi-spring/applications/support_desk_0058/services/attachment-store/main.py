import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from attachment_store import router as attachment_store_router
from normalize_batch import router as normalize_batch_router
from resolve_record import router as resolve_record_router
from fetch_batch import router as fetch_batch_router
from render_profile import router as render_profile_router
from fetch_checkpoint import router as fetch_checkpoint_router
from publish_batch import router as publish_batch_router
from summarize_bundle import router as summarize_bundle_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(attachment_store_router)
app.include_router(normalize_batch_router)
app.include_router(resolve_record_router)
app.include_router(fetch_batch_router)
app.include_router(render_profile_router)
app.include_router(fetch_checkpoint_router)
app.include_router(publish_batch_router)
app.include_router(summarize_bundle_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
