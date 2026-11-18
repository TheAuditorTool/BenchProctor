# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
from dataclasses import dataclass
from fastapi.responses import JSONResponse


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


@app.post("/BenchmarkTest00134")
async def BenchmarkTest00134(request: Request):
    auth_header = request.headers.get('authorization', '')
    form = FormData(payload=auth_header)
    data = form.payload
    return RedirectResponse(url=str(data))
