# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from jinja2 import Environment


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00088")
async def BenchmarkTest00088(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(processed))
    return HTMLResponse(page)
