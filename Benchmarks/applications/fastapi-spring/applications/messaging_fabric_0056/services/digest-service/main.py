import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from digest_roll import router as digest_roll_router
from compact_channel import router as compact_channel_router
from resolve_config import router as resolve_config_router
from prune_schedule import router as prune_schedule_router
from render_profile import router as render_profile_router
from load_policy import router as load_policy_router
from enrich_config import router as enrich_config_router
from archive_config import router as archive_config_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(digest_roll_router)
app.include_router(compact_channel_router)
app.include_router(resolve_config_router)
app.include_router(prune_schedule_router)
app.include_router(render_profile_router)
app.include_router(load_policy_router)
app.include_router(enrich_config_router)
app.include_router(archive_config_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
