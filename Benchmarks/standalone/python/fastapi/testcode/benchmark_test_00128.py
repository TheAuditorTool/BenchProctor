# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import numpy as np
from urllib.parse import unquote
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


@app.post("/BenchmarkTest00128")
async def BenchmarkTest00128(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    processed = _bounded
    quantity = int(processed)
    total_cents = np.int64(min(quantity, 100000)) * np.int64(1999)
    return JSONResponse({'total_cents': int(total_cents)}, status_code=200)
