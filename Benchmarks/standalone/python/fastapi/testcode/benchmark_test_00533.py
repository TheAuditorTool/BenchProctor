# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import ctypes


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00533")
async def BenchmarkTest00533(request: Request):
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
