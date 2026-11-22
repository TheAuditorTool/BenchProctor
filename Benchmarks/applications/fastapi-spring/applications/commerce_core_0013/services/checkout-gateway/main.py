import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from checkout_session import router as checkout_session_router
from publish_schedule import router as publish_schedule_router
from compact_threshold import router as compact_threshold_router
from annotate_order import router as annotate_order_router
from normalize_receipt import router as normalize_receipt_router
from reconcile_policy import router as reconcile_policy_router
from rotate_index import router as rotate_index_router
from audit_roster import router as audit_roster_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(checkout_session_router)
app.include_router(publish_schedule_router)
app.include_router(compact_threshold_router)
app.include_router(annotate_order_router)
app.include_router(normalize_receipt_router)
app.include_router(reconcile_policy_router)
app.include_router(rotate_index_router)
app.include_router(audit_roster_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
