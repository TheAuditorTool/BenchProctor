import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from preview_render import router as preview_render_router
from render_ledger import router as render_ledger_router
from load_config import router as load_config_router
from archive_record import router as archive_record_router
from build_ledger import router as build_ledger_router
from publish_article import router as publish_article_router
from validate_taxonomy import router as validate_taxonomy_router
from build_window import router as build_window_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(preview_render_router)
app.include_router(render_ledger_router)
app.include_router(load_config_router)
app.include_router(archive_record_router)
app.include_router(build_ledger_router)
app.include_router(publish_article_router)
app.include_router(validate_taxonomy_router)
app.include_router(build_window_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
