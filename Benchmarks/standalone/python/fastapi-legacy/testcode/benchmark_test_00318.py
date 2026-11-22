# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from jinja2 import Environment
from starlette.responses import HTMLResponse
from urllib.parse import unquote
from fastapi import Form
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


@app.post("/BenchmarkTest00318")
async def BenchmarkTest00318(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    page = Environment(autoescape=True).from_string('<div>{{ value }}</div>').render(value=str(data))
    return HTMLResponse(page)
