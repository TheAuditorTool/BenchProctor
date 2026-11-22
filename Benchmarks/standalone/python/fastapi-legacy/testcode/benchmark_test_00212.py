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


@app.post("/BenchmarkTest00212")
async def BenchmarkTest00212(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    if match is None:
        return JSONResponse({'error': 'not an email address'}, status_code=400)
    domain = match.group(1)
    return JSONResponse({'domain': domain}, status_code=200)
