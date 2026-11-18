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


@app.post("/BenchmarkTest00663")
async def BenchmarkTest00663(request: Request):
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(upload_name).strip()
        case _:
            data = str(upload_name)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
