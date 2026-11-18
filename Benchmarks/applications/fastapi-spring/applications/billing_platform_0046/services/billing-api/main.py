import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from invoice_intake import router as invoice_intake_router
from archive_record import router as archive_record_router
from load_roster import router as load_roster_router
from resolve_profile import router as resolve_profile_router
from prune_profile import router as prune_profile_router
from annotate_window import router as annotate_window_router
from normalize_index import router as normalize_index_router
from prune_record import router as prune_record_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(invoice_intake_router)
app.include_router(archive_record_router)
app.include_router(load_roster_router)
app.include_router(resolve_profile_router)
app.include_router(prune_profile_router)
app.include_router(annotate_window_router)
app.include_router(normalize_index_router)
app.include_router(prune_record_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
