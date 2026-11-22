# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import html
from starlette.responses import HTMLResponse
from jinja2 import Environment
from fastapi.responses import JSONResponse


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
    header_value = request.headers.get('x-custom-header', '')
    data = '{}'.format(header_value)
    processed = html.escape(data)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(processed))
    return HTMLResponse(page)
