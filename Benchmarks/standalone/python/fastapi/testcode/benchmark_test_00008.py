# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import yaml
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


@app.post("/BenchmarkTest00008")
async def BenchmarkTest00008(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
