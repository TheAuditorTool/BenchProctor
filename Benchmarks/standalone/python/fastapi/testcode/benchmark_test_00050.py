# SPDX-License-Identifier: Apache-2.0
import os
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


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


@app.post("/BenchmarkTest00050")
async def BenchmarkTest00050(request: Request):
    host_value = request.headers.get('host', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(host_value).strip()
        case _:
            data = str(host_value)
    request.session['data'] = str(data)
    return {"updated": True}
