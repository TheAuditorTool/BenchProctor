import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from archive_store import router as archive_store_router
from annotate_redaction import router as annotate_redaction_router
from annotate_receipt import router as annotate_receipt_router
from merge_conversion import router as merge_conversion_router
from publish_manifest import router as publish_manifest_router
from verify_policy import router as verify_policy_router
from verify_conversion import router as verify_conversion_router
from audit_batch import router as audit_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(archive_store_router)
app.include_router(annotate_redaction_router)
app.include_router(annotate_receipt_router)
app.include_router(merge_conversion_router)
app.include_router(publish_manifest_router)
app.include_router(verify_policy_router)
app.include_router(verify_conversion_router)
app.include_router(audit_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
