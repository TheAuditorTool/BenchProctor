import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from order_submit import router as order_submit_router
from load_policy import router as load_policy_router
from audit_roster import router as audit_roster_router
from render_profile import router as render_profile_router
from rotate_window import router as rotate_window_router
from compact_policy import router as compact_policy_router
from build_checkpoint import router as build_checkpoint_router
from verify_promotion import router as verify_promotion_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(order_submit_router)
app.include_router(load_policy_router)
app.include_router(audit_roster_router)
app.include_router(render_profile_router)
app.include_router(rotate_window_router)
app.include_router(compact_policy_router)
app.include_router(build_checkpoint_router)
app.include_router(verify_promotion_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
