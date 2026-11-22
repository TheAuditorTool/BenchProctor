# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import re
from pathlib import Path


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00264")
async def BenchmarkTest00264(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if not re.fullmatch("^(asc|desc|name|created)$", str(cookie_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = cookie_value
    Path('/var/app/data/' + str(processed)).write_text('data')
    return {"updated": True}
