# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
import ctypes


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


@app.post("/BenchmarkTest00167")
async def BenchmarkTest00167(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    form = FormData(payload=raw_body)
    data = form.payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
