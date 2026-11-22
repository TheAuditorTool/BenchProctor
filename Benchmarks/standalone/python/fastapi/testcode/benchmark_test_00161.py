# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from jinja2 import Environment
from fastapi.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00161")
async def BenchmarkTest00161(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    page = Environment(autoescape=True).from_string('<div>{{ value|safe }}</div>').render(value=str(data))
    return HTMLResponse(page)
