# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import yaml
from starlette.responses import JSONResponse
import os
import redis


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


@app.post("/BenchmarkTest00237")
async def BenchmarkTest00237(request: Request):
    redis_value = redis_client.get('user_data')
    data = '{}'.format(redis_value)
    parsed = yaml.safe_load(data)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
