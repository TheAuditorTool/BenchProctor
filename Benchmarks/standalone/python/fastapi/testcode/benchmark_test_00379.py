# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import os
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00379")
async def BenchmarkTest00379(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, raw_body))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
