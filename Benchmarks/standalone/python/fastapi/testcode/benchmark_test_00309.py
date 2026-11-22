# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import re
from dataclasses import dataclass
from starlette.responses import JSONResponse


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


@app.post("/BenchmarkTest00309")
async def BenchmarkTest00309(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    form = FormData(payload=raw_body)
    data = form.payload
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    domain = match.group(1)
    return JSONResponse({'domain': domain}, status_code=200)
