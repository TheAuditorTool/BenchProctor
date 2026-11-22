# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import numpy as np
import os
from starlette.responses import JSONResponse
import json


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00125")
async def BenchmarkTest00125(request: Request):
    env_value = os.environ.get('APP_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    quantity = int(str(data))
    total_cents = np.int32(quantity) * np.int32(1999)
    return JSONResponse({'total_cents': int(total_cents)}, status_code=200)
