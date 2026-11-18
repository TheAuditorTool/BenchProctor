# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import base64
import pickle
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


@app.post("/BenchmarkTest00082")
async def BenchmarkTest00082(request: Request):
    redis_value = redis_client.get('user_data')
    data = str(redis_value).replace('\x00', '')
    pickle.loads(base64.b64decode(data))
    return {"updated": True}
