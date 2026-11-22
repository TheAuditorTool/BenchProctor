# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import os
from sqlalchemy import create_engine
from fastapi.responses import JSONResponse


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
    header_value = request.headers.get('x-custom-header', '')
    parts = str(header_value).split(',')
    data = ' '.join(parts)
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': data})
    return {"updated": True}
