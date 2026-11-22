# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import hashlib
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


@app.post("/BenchmarkTest00052")
async def BenchmarkTest00052(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    kind = 'json' if str(comment_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(comment_value).strip()
        case _:
            data = str(comment_value)
    digest = hashlib.sha3_256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
