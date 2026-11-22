import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from search_index import router as search_index_router
from annotate_report import router as annotate_report_router
from build_attachment import router as build_attachment_router
from publish_header import router as publish_header_router
from compact_config import router as compact_config_router
from format_schedule import router as format_schedule_router
from compact_signature import router as compact_signature_router
from collect_batch import router as collect_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(search_index_router)
app.include_router(annotate_report_router)
app.include_router(build_attachment_router)
app.include_router(publish_header_router)
app.include_router(compact_config_router)
app.include_router(format_schedule_router)
app.include_router(compact_signature_router)
app.include_router(collect_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
