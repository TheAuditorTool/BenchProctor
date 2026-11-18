# SPDX-License-Identifier: Apache-2.0
import os
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from pydantic import Field, ValidationError, create_model


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


@app.post("/BenchmarkTest00475")
async def BenchmarkTest00475(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.\\-]+$")))(value=str(data))
    except ValidationError:
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    request.session['data'] = str(processed)
    return {"updated": True}
