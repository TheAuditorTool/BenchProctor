# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import random
from starlette.responses import JSONResponse
from app_runtime import db


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00698")
async def BenchmarkTest00698(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JSONResponse({'token': str(token)}, status_code=200)
