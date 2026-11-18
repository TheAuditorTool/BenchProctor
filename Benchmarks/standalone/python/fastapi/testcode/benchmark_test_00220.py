# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
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


@app.post("/BenchmarkTest00220")
async def BenchmarkTest00220(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    form = FormData(payload=db_value)
    data = form.payload
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return JSONResponse({'error': 'not found'}, status_code=404)
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
