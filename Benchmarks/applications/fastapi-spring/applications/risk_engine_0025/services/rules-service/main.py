import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from rule_evaluate import router as rule_evaluate_router
from verify_checkpoint import router as verify_checkpoint_router
from format_digest import router as format_digest_router
from prune_snapshot import router as prune_snapshot_router
from archive_roster import router as archive_roster_router
from build_case import router as build_case_router
from fetch_roster import router as fetch_roster_router
from archive_receipt import router as archive_receipt_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(rule_evaluate_router)
app.include_router(verify_checkpoint_router)
app.include_router(format_digest_router)
app.include_router(prune_snapshot_router)
app.include_router(archive_roster_router)
app.include_router(build_case_router)
app.include_router(fetch_roster_router)
app.include_router(archive_receipt_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
