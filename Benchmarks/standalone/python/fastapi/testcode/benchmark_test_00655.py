# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import json
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


@app.post("/BenchmarkTest00655")
async def BenchmarkTest00655(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
