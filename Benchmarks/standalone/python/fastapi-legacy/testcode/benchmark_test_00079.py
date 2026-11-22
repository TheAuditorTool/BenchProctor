# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import json
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


@app.post("/BenchmarkTest00079/{id}")
async def BenchmarkTest00079(request: Request, id: str):
    path_value = id
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return {"updated": True}
