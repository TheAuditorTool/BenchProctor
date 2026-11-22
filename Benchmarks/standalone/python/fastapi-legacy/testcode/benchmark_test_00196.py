# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ctypes
from fastapi import Form
from starlette.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00196")
async def BenchmarkTest00196(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    processed = _bounded
    count = int(processed)
    records = ctypes.create_string_buffer(min(count, 65536) * 64)
    return JSONResponse({'allocated': len(records)}, status_code=200)
