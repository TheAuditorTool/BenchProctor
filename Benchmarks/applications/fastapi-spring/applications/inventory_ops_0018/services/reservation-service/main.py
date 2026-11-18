import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from reservation_hold import router as reservation_hold_router
from format_header import router as format_header_router
from annotate_report import router as annotate_report_router
from verify_profile import router as verify_profile_router
from reconcile_schedule import router as reconcile_schedule_router
from normalize_schedule import router as normalize_schedule_router
from build_schedule import router as build_schedule_router
from load_reservation import router as load_reservation_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(reservation_hold_router)
app.include_router(format_header_router)
app.include_router(annotate_report_router)
app.include_router(verify_profile_router)
app.include_router(reconcile_schedule_router)
app.include_router(normalize_schedule_router)
app.include_router(build_schedule_router)
app.include_router(load_reservation_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
