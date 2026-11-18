# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import hashlib
from dataclasses import dataclass
from starlette.responses import JSONResponse
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00140")
async def BenchmarkTest00140(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    form = FormData(payload=db_value)
    data = form.payload
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
