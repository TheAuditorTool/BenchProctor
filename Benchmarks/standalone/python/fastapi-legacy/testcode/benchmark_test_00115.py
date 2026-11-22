# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
import socket
import urllib.parse
from fastapi.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

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
    data = RequestPayload(api_value).value
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return {"updated": True}
