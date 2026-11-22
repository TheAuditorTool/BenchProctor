# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import subprocess
from starlette.responses import JSONResponse
import re


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00049")
async def BenchmarkTest00049(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if not re.fullmatch("^(asc|desc|name|created)$", str(header_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = header_value
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
