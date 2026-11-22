import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from service_register import router as service_register_router
from publish_snapshot import router as publish_snapshot_router
from load_record import router as load_record_router
from resolve_bundle import router as resolve_bundle_router
from rotate_record import router as rotate_record_router
from publish_checkpoint import router as publish_checkpoint_router
from collect_report import router as collect_report_router
from load_receipt import router as load_receipt_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(service_register_router)
app.include_router(publish_snapshot_router)
app.include_router(load_record_router)
app.include_router(resolve_bundle_router)
app.include_router(rotate_record_router)
app.include_router(publish_checkpoint_router)
app.include_router(collect_report_router)
app.include_router(load_receipt_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
