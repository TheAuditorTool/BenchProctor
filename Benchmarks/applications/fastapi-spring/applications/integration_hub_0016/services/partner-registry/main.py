import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from partner_register import router as partner_register_router
from render_webhook import router as render_webhook_router
from prune_checkpoint import router as prune_checkpoint_router
from rotate_digest import router as rotate_digest_router
from compact_policy import router as compact_policy_router
from render_window import router as render_window_router
from load_schedule import router as load_schedule_router
from prune_batch import router as prune_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(partner_register_router)
app.include_router(render_webhook_router)
app.include_router(prune_checkpoint_router)
app.include_router(rotate_digest_router)
app.include_router(compact_policy_router)
app.include_router(render_window_router)
app.include_router(load_schedule_router)
app.include_router(prune_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
