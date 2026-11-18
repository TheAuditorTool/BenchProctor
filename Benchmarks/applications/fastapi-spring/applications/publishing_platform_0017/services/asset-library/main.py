import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from asset_attach import router as asset_attach_router
from collect_syndication import router as collect_syndication_router
from fetch_batch import router as fetch_batch_router
from verify_digest import router as verify_digest_router
from fetch_header import router as fetch_header_router
from render_article import router as render_article_router
from resolve_batch import router as resolve_batch_router
from audit_header import router as audit_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(asset_attach_router)
app.include_router(collect_syndication_router)
app.include_router(fetch_batch_router)
app.include_router(verify_digest_router)
app.include_router(fetch_header_router)
app.include_router(render_article_router)
app.include_router(resolve_batch_router)
app.include_router(audit_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
