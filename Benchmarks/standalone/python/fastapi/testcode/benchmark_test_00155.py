# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
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


@app.post("/BenchmarkTest00155")
async def BenchmarkTest00155(request: Request, field: str = Form('')):
    field_value = field
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(field_value),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
