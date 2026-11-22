# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from Crypto.Hash import MD4
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


@app.post("/BenchmarkTest00129")
async def BenchmarkTest00129(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    digest = MD4.new(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
