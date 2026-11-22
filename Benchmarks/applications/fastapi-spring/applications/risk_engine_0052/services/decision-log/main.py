import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from decision_record import router as decision_record_router
from render_policy import router as render_policy_router
from format_batch import router as format_batch_router
from prune_receipt import router as prune_receipt_router
from normalize_batch import router as normalize_batch_router
from audit_window import router as audit_window_router
from resolve_window import router as resolve_window_router
from rotate_case import router as rotate_case_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(decision_record_router)
app.include_router(render_policy_router)
app.include_router(format_batch_router)
app.include_router(prune_receipt_router)
app.include_router(normalize_batch_router)
app.include_router(audit_window_router)
app.include_router(resolve_window_router)
app.include_router(rotate_case_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
