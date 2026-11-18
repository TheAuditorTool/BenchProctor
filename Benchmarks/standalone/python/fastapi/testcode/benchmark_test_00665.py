# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pathlib import Path
from dataclasses import dataclass
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
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


@app.post("/BenchmarkTest00665")
async def BenchmarkTest00665(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    form = FormData(payload=db_value)
    data = form.payload
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
