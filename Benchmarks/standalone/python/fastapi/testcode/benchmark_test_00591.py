# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import os
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00591")
async def BenchmarkTest00591(request: Request):
    env_value = os.environ.get('APP_INPUT', '')
    data = RequestPayload(env_value).value
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    processed = _bounded
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JSONResponse({'allocated': allocated}, status_code=200)
