# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from dataclasses import dataclass


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


@app.post("/BenchmarkTest00648")
async def BenchmarkTest00648(request: Request):
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    form = FormData(payload=upload_name)
    data = form.payload
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
