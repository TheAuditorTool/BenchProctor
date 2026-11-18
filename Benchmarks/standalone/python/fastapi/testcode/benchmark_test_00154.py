# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from app_runtime import db
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


@app.post("/BenchmarkTest00154")
async def BenchmarkTest00154(request: Request):
    redis_value = redis_client.get('user_data')
    data = str(redis_value).replace('\x00', '')
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    processed = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
