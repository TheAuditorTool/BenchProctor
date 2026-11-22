import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from return_request import router as return_request_router
from archive_window import router as archive_window_router
from normalize_checkpoint import router as normalize_checkpoint_router
from validate_header import router as validate_header_router
from collect_fulfillment import router as collect_fulfillment_router
from rotate_fulfillment import router as rotate_fulfillment_router
from enrich_profile import router as enrich_profile_router
from format_header import router as format_header_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(return_request_router)
app.include_router(archive_window_router)
app.include_router(normalize_checkpoint_router)
app.include_router(validate_header_router)
app.include_router(collect_fulfillment_router)
app.include_router(rotate_fulfillment_router)
app.include_router(enrich_profile_router)
app.include_router(format_header_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
