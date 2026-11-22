# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from Crypto.Hash import SHA256
from fastapi import Form
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


@app.post("/BenchmarkTest00295")
async def BenchmarkTest00295(request: Request, field: str = Form('')):
    field_value = field
    digest = SHA256.new(str(field_value).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
