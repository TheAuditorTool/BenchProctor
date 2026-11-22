# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import StreamingResponse
import re
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00171")
async def BenchmarkTest00171(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return StreamingResponse(iter(['<div>' + str(processed) + '</div>']), media_type='text/html')
