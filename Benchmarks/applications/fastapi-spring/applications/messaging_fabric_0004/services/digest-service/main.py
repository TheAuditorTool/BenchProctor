import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from digest_roll import router as digest_roll_router
from verify_schedule import router as verify_schedule_router
from annotate_profile import router as annotate_profile_router
from validate_batch import router as validate_batch_router
from verify_subscription import router as verify_subscription_router
from rotate_delivery import router as rotate_delivery_router
from verify_policy import router as verify_policy_router
from compact_batch import router as compact_batch_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(digest_roll_router)
app.include_router(verify_schedule_router)
app.include_router(annotate_profile_router)
app.include_router(validate_batch_router)
app.include_router(verify_subscription_router)
app.include_router(rotate_delivery_router)
app.include_router(verify_policy_router)
app.include_router(compact_batch_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
