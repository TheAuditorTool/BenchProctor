import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from service_register import router as service_register_router
from verify_schedule import router as verify_schedule_router
from verify_receipt import router as verify_receipt_router
from rotate_batch import router as rotate_batch_router
from resolve_config import router as resolve_config_router
from resolve_batch import router as resolve_batch_router
from verify_checkpoint import router as verify_checkpoint_router
from summarize_index import router as summarize_index_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(service_register_router)
app.include_router(verify_schedule_router)
app.include_router(verify_receipt_router)
app.include_router(rotate_batch_router)
app.include_router(resolve_config_router)
app.include_router(resolve_batch_router)
app.include_router(verify_checkpoint_router)
app.include_router(summarize_index_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
