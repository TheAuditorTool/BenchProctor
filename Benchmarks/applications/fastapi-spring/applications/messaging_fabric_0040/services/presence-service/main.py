import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from presence_update import router as presence_update_router
from verify_header import router as verify_header_router
from export_roster import router as export_roster_router
from annotate_receipt import router as annotate_receipt_router
from collect_schedule import router as collect_schedule_router
from compact_schedule import router as compact_schedule_router
from fetch_record import router as fetch_record_router
from audit_schedule import router as audit_schedule_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(presence_update_router)
app.include_router(verify_header_router)
app.include_router(export_roster_router)
app.include_router(annotate_receipt_router)
app.include_router(collect_schedule_router)
app.include_router(compact_schedule_router)
app.include_router(fetch_record_router)
app.include_router(audit_schedule_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
