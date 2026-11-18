# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
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


@app.post("/BenchmarkTest00445")
async def BenchmarkTest00445(request: Request, field: str = Form('')):
    field_value = field
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(field_value).strip()
        case _:
            data = str(field_value)
    requests.get(str(data))
    return {"updated": True}
