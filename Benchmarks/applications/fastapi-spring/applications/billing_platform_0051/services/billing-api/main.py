import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from invoice_intake import router as invoice_intake_router
from verify_ledger import router as verify_ledger_router
from rotate_invoice import router as rotate_invoice_router
from archive_index import router as archive_index_router
from validate_summary import router as validate_summary_router
from load_roster import router as load_roster_router
from export_dunning import router as export_dunning_router
from export_batch import router as export_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(invoice_intake_router)
app.include_router(verify_ledger_router)
app.include_router(rotate_invoice_router)
app.include_router(archive_index_router)
app.include_router(validate_summary_router)
app.include_router(load_roster_router)
app.include_router(export_dunning_router)
app.include_router(export_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
