# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
from fastapi.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00067")
async def BenchmarkTest00067(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    requests.get(str(data))
    return {"updated": True}
