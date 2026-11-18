# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import ctypes


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


@app.post("/BenchmarkTest00008")
async def BenchmarkTest00008(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
