# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ctypes
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


@app.post("/BenchmarkTest00283")
async def BenchmarkTest00283(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = RequestPayload(ua_value).value
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    processed = _bounded
    count = int(processed)
    records = ctypes.create_string_buffer(min(count, 65536) * 64)
    return JSONResponse({'allocated': len(records)}, status_code=200)
