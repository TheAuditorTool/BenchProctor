import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from fx_convert import router as fx_convert_router
from compact_digest import router as compact_digest_router
from normalize_ledger import router as normalize_ledger_router
from summarize_wallet import router as summarize_wallet_router
from render_window import router as render_window_router
from resolve_wallet import router as resolve_wallet_router
from merge_bundle import router as merge_bundle_router
from archive_report import router as archive_report_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(fx_convert_router)
app.include_router(compact_digest_router)
app.include_router(normalize_ledger_router)
app.include_router(summarize_wallet_router)
app.include_router(render_window_router)
app.include_router(resolve_wallet_router)
app.include_router(merge_bundle_router)
app.include_router(archive_report_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
