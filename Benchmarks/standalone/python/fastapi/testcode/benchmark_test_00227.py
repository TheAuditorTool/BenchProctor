# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import json
import os
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00227")
async def BenchmarkTest00227(request: Request):
    env_value = os.environ.get('APP_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    parsed = json.loads(data)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
