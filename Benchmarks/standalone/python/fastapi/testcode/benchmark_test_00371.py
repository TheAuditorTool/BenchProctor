# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import defusedxml.ElementTree
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


@app.post("/BenchmarkTest00371")
async def BenchmarkTest00371(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = RequestPayload(xml_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
