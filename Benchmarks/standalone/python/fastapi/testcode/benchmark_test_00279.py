# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import urllib.request
from fastapi import Form
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


@app.post("/BenchmarkTest00279")
async def BenchmarkTest00279(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    outbound = urllib.request.Request(str(data), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
