# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from fastapi import Form
import defusedxml.ElementTree
from fastapi.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00040")
async def BenchmarkTest00040(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
