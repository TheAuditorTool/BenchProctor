# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import secrets
from fastapi import Form
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


@app.post("/BenchmarkTest00179")
async def BenchmarkTest00179(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    token = secrets.token_bytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JSONResponse({'token': str(token)}, status_code=200)
