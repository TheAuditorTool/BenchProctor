# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import numpy as np
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


@app.post("/BenchmarkTest00306")
async def BenchmarkTest00306(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    processed = _bounded
    quantity = int(processed)
    total_cents = np.int64(min(quantity, 100000)) * np.int64(1999)
    return JSONResponse({'total_cents': int(total_cents)}, status_code=200)
