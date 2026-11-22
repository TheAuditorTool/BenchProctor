# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import os
from sqlalchemy import create_engine


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


@app.post("/BenchmarkTest00187")
async def BenchmarkTest00187(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = bytes.fromhex(file_value).decode('utf-8', 'ignore')
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    processed = _coerced
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
