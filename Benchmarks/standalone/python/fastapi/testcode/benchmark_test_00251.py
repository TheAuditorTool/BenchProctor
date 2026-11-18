# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
import os
import redis
from fastapi.responses import JSONResponse


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00251")
async def BenchmarkTest00251(request: Request):
    redis_value = redis_client.get('user_data')
    if redis_value:
        data = redis_value
    else:
        data = ''
    requests.get(str(data))
    return {"updated": True}
