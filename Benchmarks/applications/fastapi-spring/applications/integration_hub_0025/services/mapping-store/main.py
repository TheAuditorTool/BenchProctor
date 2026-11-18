import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from field_mapping import router as field_mapping_router
from archive_record import router as archive_record_router
from merge_policy import router as merge_policy_router
from verify_config import router as verify_config_router
from publish_report import router as publish_report_router
from enrich_checkpoint import router as enrich_checkpoint_router
from archive_receipt import router as archive_receipt_router
from rotate_receipt import router as rotate_receipt_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(field_mapping_router)
app.include_router(archive_record_router)
app.include_router(merge_policy_router)
app.include_router(verify_config_router)
app.include_router(publish_report_router)
app.include_router(enrich_checkpoint_router)
app.include_router(archive_receipt_router)
app.include_router(rotate_receipt_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
