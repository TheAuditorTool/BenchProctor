# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from urllib.parse import urlparse
import requests
from starlette.responses import JSONResponse
import socket
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


@app.post("/BenchmarkTest00086")
async def BenchmarkTest00086(request: Request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data, _sep, _rest = str(api_value).partition('\x00')
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
