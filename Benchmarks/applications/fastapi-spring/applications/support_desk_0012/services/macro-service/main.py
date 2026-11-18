import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from macro_apply import router as macro_apply_router
from compact_batch import router as compact_batch_router
from load_config import router as load_config_router
from normalize_roster import router as normalize_roster_router
from merge_summary import router as merge_summary_router
from export_policy import router as export_policy_router
from annotate_report import router as annotate_report_router
from fetch_digest import router as fetch_digest_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(macro_apply_router)
app.include_router(compact_batch_router)
app.include_router(load_config_router)
app.include_router(normalize_roster_router)
app.include_router(merge_summary_router)
app.include_router(export_policy_router)
app.include_router(annotate_report_router)
app.include_router(fetch_digest_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
