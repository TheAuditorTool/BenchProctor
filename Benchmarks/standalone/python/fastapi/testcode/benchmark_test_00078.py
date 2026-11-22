# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pathlib import Path
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


@app.post("/BenchmarkTest00078")
async def BenchmarkTest00078(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = RequestPayload(header_value).value
    Path('/var/app/data/' + str(data)).write_text('data')
    return {"updated": True}
