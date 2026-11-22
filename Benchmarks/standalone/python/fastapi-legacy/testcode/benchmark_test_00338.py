# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from jinja2 import Environment
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


@app.post("/BenchmarkTest00338")
async def BenchmarkTest00338(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(processed))
    return HTMLResponse(page)
