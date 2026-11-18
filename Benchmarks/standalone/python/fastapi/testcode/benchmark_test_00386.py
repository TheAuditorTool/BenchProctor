# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import json
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


@app.post("/BenchmarkTest00386")
async def BenchmarkTest00386(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parsed = json.loads(cookie_value)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
