# SPDX-License-Identifier: Apache-2.0
import os
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
from fastapi import Form
from starlette.responses import JSONResponse
from pydantic import Field, ValidationError, create_model


def make_reader(raw):
    def read():
        return raw.strip()
    return read

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


@app.post("/BenchmarkTest00511")
async def BenchmarkTest00511(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.\\-]+$")))(value=str(data))
    except ValidationError:
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    request.session['data'] = str(processed)
    return {"updated": True}
