import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from case_open import router as case_open_router
from fetch_case import router as fetch_case_router
from build_summary import router as build_summary_router
from rotate_screening import router as rotate_screening_router
from reconcile_threshold import router as reconcile_threshold_router
from load_index import router as load_index_router
from collect_record import router as collect_record_router
from validate_digest import router as validate_digest_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(case_open_router)
app.include_router(fetch_case_router)
app.include_router(build_summary_router)
app.include_router(rotate_screening_router)
app.include_router(reconcile_threshold_router)
app.include_router(load_index_router)
app.include_router(collect_record_router)
app.include_router(validate_digest_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
