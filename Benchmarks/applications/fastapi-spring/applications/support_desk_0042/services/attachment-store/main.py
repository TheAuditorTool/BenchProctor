import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from attachment_store import router as attachment_store_router
from build_macro import router as build_macro_router
from rotate_bundle import router as rotate_bundle_router
from fetch_ticket import router as fetch_ticket_router
from export_policy import router as export_policy_router
from publish_manifest import router as publish_manifest_router
from publish_header import router as publish_header_router
from format_header import router as format_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(attachment_store_router)
app.include_router(build_macro_router)
app.include_router(rotate_bundle_router)
app.include_router(fetch_ticket_router)
app.include_router(export_policy_router)
app.include_router(publish_manifest_router)
app.include_router(publish_header_router)
app.include_router(format_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
