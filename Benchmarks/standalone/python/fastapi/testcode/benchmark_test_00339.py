# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import re
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


@app.post("/BenchmarkTest00339")
async def BenchmarkTest00339(request: Request):
    host_value = request.headers.get('host', '')
    match = re.match(r'^[^@]+@([^@]+)$', str(host_value))
    domain = match.group(1)
    return JSONResponse({'domain': domain}, status_code=200)
