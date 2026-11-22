import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from thumbnail_render import router as thumbnail_render_router
from merge_receipt import router as merge_receipt_router
from normalize_receipt import router as normalize_receipt_router
from collect_policy import router as collect_policy_router
from resolve_policy import router as resolve_policy_router
from collect_record import router as collect_record_router
from render_asset import router as render_asset_router
from prune_checkpoint import router as prune_checkpoint_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(thumbnail_render_router)
app.include_router(merge_receipt_router)
app.include_router(normalize_receipt_router)
app.include_router(collect_policy_router)
app.include_router(resolve_policy_router)
app.include_router(collect_record_router)
app.include_router(render_asset_router)
app.include_router(prune_checkpoint_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
