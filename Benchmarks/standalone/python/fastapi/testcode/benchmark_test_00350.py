# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from app_runtime import db
from fastapi.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00350")
async def BenchmarkTest00350(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return {"updated": True}
