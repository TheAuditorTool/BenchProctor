# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import socket
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


@app.post("/BenchmarkTest00334")
async def BenchmarkTest00334(request: Request):
    redis_value = redis_client.get('user_data')
    data = f'{redis_value!s}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
