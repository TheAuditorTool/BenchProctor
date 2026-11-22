# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
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


@app.post("/BenchmarkTest00311")
async def BenchmarkTest00311(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    parsed = json.loads(data)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
