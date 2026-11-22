import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from order_submit import router as order_submit_router
from format_batch import router as format_batch_router
from normalize_promotion import router as normalize_promotion_router
from annotate_promotion import router as annotate_promotion_router
from publish_config import router as publish_config_router
from reconcile_bundle import router as reconcile_bundle_router
from render_header import router as render_header_router
from validate_schedule import router as validate_schedule_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(order_submit_router)
app.include_router(format_batch_router)
app.include_router(normalize_promotion_router)
app.include_router(annotate_promotion_router)
app.include_router(publish_config_router)
app.include_router(reconcile_bundle_router)
app.include_router(render_header_router)
app.include_router(validate_schedule_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
