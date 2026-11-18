import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from template_compose import router as template_compose_router
from render_profile import router as render_profile_router
from rotate_delivery import router as rotate_delivery_router
from validate_schedule import router as validate_schedule_router
from validate_policy import router as validate_policy_router
from validate_message import router as validate_message_router
from annotate_schedule import router as annotate_schedule_router
from load_record import router as load_record_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(template_compose_router)
app.include_router(render_profile_router)
app.include_router(rotate_delivery_router)
app.include_router(validate_schedule_router)
app.include_router(validate_policy_router)
app.include_router(validate_message_router)
app.include_router(annotate_schedule_router)
app.include_router(load_record_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
