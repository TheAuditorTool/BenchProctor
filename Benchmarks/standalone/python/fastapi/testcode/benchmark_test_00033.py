# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from pydantic import BaseModel
import defusedxml.ElementTree
from fastapi.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
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


@app.post("/BenchmarkTest00033")
async def BenchmarkTest00033(request: Request, req: UserInput):
    json_value = req.payload
    data = RequestPayload(json_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
