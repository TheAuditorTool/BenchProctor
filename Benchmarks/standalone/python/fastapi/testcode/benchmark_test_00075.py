# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import base64
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


@app.post("/BenchmarkTest00075")
async def BenchmarkTest00075(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(data) + "'")
    return {"updated": True}
