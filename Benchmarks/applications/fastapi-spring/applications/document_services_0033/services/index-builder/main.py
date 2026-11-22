import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from search_index import router as search_index_router
from rotate_conversion import router as rotate_conversion_router
from rotate_schedule import router as rotate_schedule_router
from publish_schedule import router as publish_schedule_router
from enrich_receipt import router as enrich_receipt_router
from fetch_record import router as fetch_record_router
from render_threshold import router as render_threshold_router
from format_profile import router as format_profile_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(search_index_router)
app.include_router(rotate_conversion_router)
app.include_router(rotate_schedule_router)
app.include_router(publish_schedule_router)
app.include_router(enrich_receipt_router)
app.include_router(fetch_record_router)
app.include_router(render_threshold_router)
app.include_router(format_profile_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
