# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from jinja2 import Environment
from starlette.responses import HTMLResponse
from pydantic import BaseModel
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


@app.post("/BenchmarkTest00269")
async def BenchmarkTest00269(request: Request, req: UserInput):
    json_value = req.payload
    data, _sep, _rest = str(json_value).partition('\x00')
    page = Environment(autoescape=True).from_string('<div>{{ value }}</div>').render(value=str(data))
    return HTMLResponse(page)
