import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from secret_fetch import router as secret_fetch_router
from collect_record import router as collect_record_router
from normalize_flag import router as normalize_flag_router
from archive_digest import router as archive_digest_router
from reconcile_config import router as reconcile_config_router
from publish_quota import router as publish_quota_router
from normalize_roster import router as normalize_roster_router
from resolve_batch import router as resolve_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(secret_fetch_router)
app.include_router(collect_record_router)
app.include_router(normalize_flag_router)
app.include_router(archive_digest_router)
app.include_router(reconcile_config_router)
app.include_router(publish_quota_router)
app.include_router(normalize_roster_router)
app.include_router(resolve_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
