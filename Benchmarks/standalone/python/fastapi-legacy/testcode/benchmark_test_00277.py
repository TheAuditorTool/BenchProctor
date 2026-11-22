# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import secrets
import base64
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


@app.post("/BenchmarkTest00277")
async def BenchmarkTest00277(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    token = secrets.token_bytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JSONResponse({'token': str(token)}, status_code=200)
