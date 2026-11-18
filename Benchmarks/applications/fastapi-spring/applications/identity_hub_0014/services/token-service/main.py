import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from token_mint import router as token_mint_router
from export_index import router as export_index_router
from enrich_manifest import router as enrich_manifest_router
from export_header import router as export_header_router
from compact_ledger import router as compact_ledger_router
from fetch_manifest import router as fetch_manifest_router
from merge_manifest import router as merge_manifest_router
from fetch_roster import router as fetch_roster_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(token_mint_router)
app.include_router(export_index_router)
app.include_router(enrich_manifest_router)
app.include_router(export_header_router)
app.include_router(compact_ledger_router)
app.include_router(fetch_manifest_router)
app.include_router(merge_manifest_router)
app.include_router(fetch_roster_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
