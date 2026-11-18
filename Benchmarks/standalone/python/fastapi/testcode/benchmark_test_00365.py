# SPDX-License-Identifier: Apache-2.0
import os
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from app_runtime import db


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


@app.post("/BenchmarkTest00365")
async def BenchmarkTest00365(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid number'}, status_code=400)
    processed = _coerced
    request.session['data'] = str(processed)
    return {"updated": True}
