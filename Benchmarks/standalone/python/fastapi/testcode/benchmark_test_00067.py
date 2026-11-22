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


@app.post("/BenchmarkTest00067")
async def BenchmarkTest00067(request: Request):
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    data = (lambda v: v.strip())(upload_name)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return {"updated": True}
