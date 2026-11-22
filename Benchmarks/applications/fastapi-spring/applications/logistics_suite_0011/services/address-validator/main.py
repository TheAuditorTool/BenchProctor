import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from address_validate import router as address_validate_router
from normalize_index import router as normalize_index_router
from resolve_roster import router as resolve_roster_router
from format_batch import router as format_batch_router
from audit_ledger import router as audit_ledger_router
from collect_label import router as collect_label_router
from enrich_index import router as enrich_index_router
from merge_roster import router as merge_roster_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(address_validate_router)
app.include_router(normalize_index_router)
app.include_router(resolve_roster_router)
app.include_router(format_batch_router)
app.include_router(audit_ledger_router)
app.include_router(collect_label_router)
app.include_router(enrich_index_router)
app.include_router(merge_roster_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
