# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from urllib.parse import urlparse
from dataclasses import dataclass
import requests
from starlette.responses import JSONResponse
import socket
import urllib.parse
import re


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00115")
async def BenchmarkTest00115(request: Request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    form = FormData(payload=api_value)
    data = form.payload
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    s = socket.create_connection((urllib.parse.urlparse(str(target_url)).hostname, 80))
    s.close()
    return {"updated": True}
