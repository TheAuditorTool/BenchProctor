# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import os
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


@app.post("/BenchmarkTest00287")
async def BenchmarkTest00287(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
