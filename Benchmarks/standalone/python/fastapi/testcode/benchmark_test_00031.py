# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import random
from fastapi import Form
from starlette.responses import JSONResponse
import json
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


@app.post("/BenchmarkTest00031")
async def BenchmarkTest00031(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JSONResponse({'token': str(token)}, status_code=200)
