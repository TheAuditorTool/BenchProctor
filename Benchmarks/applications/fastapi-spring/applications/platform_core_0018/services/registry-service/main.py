import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from service_register import router as service_register_router
from merge_report import router as merge_report_router
from format_receipt import router as format_receipt_router
from collect_schedule import router as collect_schedule_router
from summarize_digest import router as summarize_digest_router
from rotate_tenant import router as rotate_tenant_router
from annotate_window import router as annotate_window_router
from compact_roster import router as compact_roster_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(service_register_router)
app.include_router(merge_report_router)
app.include_router(format_receipt_router)
app.include_router(collect_schedule_router)
app.include_router(summarize_digest_router)
app.include_router(rotate_tenant_router)
app.include_router(annotate_window_router)
app.include_router(compact_roster_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
