# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from urllib.parse import urlparse
import base64
from starlette.responses import JSONResponse
import socket
import re
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


@app.post("/BenchmarkTest00139")
async def BenchmarkTest00139(request: Request):
    redis_value = redis_client.get('user_data')
    data = base64.b64decode(redis_value).decode('utf-8', 'ignore')
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
