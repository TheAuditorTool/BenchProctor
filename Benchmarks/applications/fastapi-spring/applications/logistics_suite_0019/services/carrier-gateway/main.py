import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from carrier_dispatch import router as carrier_dispatch_router
from summarize_shipment import router as summarize_shipment_router
from compact_schedule import router as compact_schedule_router
from collect_threshold import router as collect_threshold_router
from merge_roster import router as merge_roster_router
from load_policy import router as load_policy_router
from verify_policy import router as verify_policy_router
from fetch_roster import router as fetch_roster_router

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(carrier_dispatch_router)
app.include_router(summarize_shipment_router)
app.include_router(compact_schedule_router)
app.include_router(collect_threshold_router)
app.include_router(merge_roster_router)
app.include_router(load_policy_router)
app.include_router(verify_policy_router)
app.include_router(fetch_roster_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
