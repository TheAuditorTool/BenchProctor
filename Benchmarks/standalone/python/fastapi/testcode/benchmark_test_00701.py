# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import hashlib
from starlette.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00701")
async def BenchmarkTest00701(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(multipart_value).strip()
        case _:
            data = str(multipart_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
