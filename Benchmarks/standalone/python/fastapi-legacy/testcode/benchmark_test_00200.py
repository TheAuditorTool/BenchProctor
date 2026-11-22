# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ctypes
from starlette.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00200")
async def BenchmarkTest00200(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return JSONResponse({'allocated': len(records)}, status_code=200)
