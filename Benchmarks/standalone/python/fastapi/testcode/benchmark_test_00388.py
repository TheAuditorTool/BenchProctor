# SPDX-License-Identifier: Apache-2.0
import os
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import re


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex())


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00388")
async def BenchmarkTest00388(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    request.session['data'] = str(processed)
    return {"updated": True}
