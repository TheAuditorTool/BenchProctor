import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from case_open import router as case_open_router
from collect_header import router as collect_header_router
from normalize_index import router as normalize_index_router
from resolve_digest import router as resolve_digest_router
from audit_summary import router as audit_summary_router
from publish_profile import router as publish_profile_router
from prune_batch import router as prune_batch_router
from collect_profile import router as collect_profile_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(case_open_router)
app.include_router(collect_header_router)
app.include_router(normalize_index_router)
app.include_router(resolve_digest_router)
app.include_router(audit_summary_router)
app.include_router(publish_profile_router)
app.include_router(prune_batch_router)
app.include_router(collect_profile_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
