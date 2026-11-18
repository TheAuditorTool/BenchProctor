# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import yaml
from fastapi.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00120")
async def BenchmarkTest00120(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
