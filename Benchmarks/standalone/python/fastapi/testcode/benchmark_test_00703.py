# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00703")
async def BenchmarkTest00703(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parsed = urlparse(header_value)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = header_value
    requests.get(str(target_url))
    return {"updated": True}
