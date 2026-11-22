# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import json
from fastapi import Form
from starlette.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00002")
async def BenchmarkTest00002(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    parsed = json.loads(data)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
