# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import re
from starlette.responses import JSONResponse
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


@app.post("/BenchmarkTest00011")
async def BenchmarkTest00011(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", ua_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = ua_value
    Path('/var/app/data/' + str(processed)).write_text('data')
    return {"updated": True}
