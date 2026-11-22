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


@app.post("/BenchmarkTest00276")
async def BenchmarkTest00276(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    if match is None:
        return JSONResponse({'error': 'not an email address'}, status_code=400)
    domain = match.group(1)
    return JSONResponse({'domain': domain}, status_code=200)
