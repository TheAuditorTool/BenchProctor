import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from token_mint import router as token_mint_router
from compact_index import router as compact_index_router
from summarize_summary import router as summarize_summary_router
from format_report import router as format_report_router
from build_batch import router as build_batch_router
from normalize_header import router as normalize_header_router
from compact_consent import router as compact_consent_router
from render_receipt import router as render_receipt_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(token_mint_router)
app.include_router(compact_index_router)
app.include_router(summarize_summary_router)
app.include_router(format_report_router)
app.include_router(build_batch_router)
app.include_router(normalize_header_router)
app.include_router(compact_consent_router)
app.include_router(render_receipt_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
