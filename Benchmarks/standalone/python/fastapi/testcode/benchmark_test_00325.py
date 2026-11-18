# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import yaml
import os
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


@app.post("/BenchmarkTest00325")
async def BenchmarkTest00325(request: Request):
    env_value = os.environ.get('APP_INPUT', '')
    data = str(env_value).replace('\x00', '')
    parsed = yaml.safe_load(data)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
