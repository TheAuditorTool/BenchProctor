# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from dataclasses import dataclass
from starlette.responses import PlainTextResponse
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


@app.post("/BenchmarkTest00430")
async def BenchmarkTest00430(request: Request):
    origin_value = request.headers.get('origin', '')
    form = FormData(payload=origin_value)
    data = form.payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
