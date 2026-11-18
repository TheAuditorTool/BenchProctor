# SPDX-License-Identifier: Apache-2.0
import os
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
from app_runtime import db
from fastapi.responses import JSONResponse


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


@app.post("/BenchmarkTest00148")
async def BenchmarkTest00148(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    request.session['data'] = str(processed)
    return {"updated": True}
