# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import secrets
from starlette.responses import JSONResponse
from app_runtime import db


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00143")
async def BenchmarkTest00143(request: Request):
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(upload_name).strip()
        case _:
            data = str(upload_name)
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JSONResponse({'token': str(token)}, status_code=200)
