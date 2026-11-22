# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import os
from sqlalchemy import create_engine


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_engine = create_engine("sqlite:///" + os.environ.get("DATABASE_PATH", "app.db"))

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00033")
async def BenchmarkTest00033(request: Request):
    referer_value = request.headers.get('referer', '')
    reader = make_reader(referer_value)
    data = reader()
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    processed = _coerced
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
