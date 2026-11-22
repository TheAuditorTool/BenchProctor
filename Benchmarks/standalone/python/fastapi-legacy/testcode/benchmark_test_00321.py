# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
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


@app.post("/BenchmarkTest00321/{id}")
async def BenchmarkTest00321(request: Request, id: str):
    path_value = id
    parts = str(path_value).split(',')
    data = ' '.join(parts)
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(data))
    return HTMLResponse(page)
