# SPDX-License-Identifier: Apache-2.0
import os
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
import re
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

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


@app.post("/BenchmarkTest00713")
async def BenchmarkTest00713(request: Request):
    referer_value = request.headers.get('referer', '')
    form = FormData(payload=referer_value)
    data = form.payload
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    request.session['data'] = str(processed)
    return {"updated": True}
