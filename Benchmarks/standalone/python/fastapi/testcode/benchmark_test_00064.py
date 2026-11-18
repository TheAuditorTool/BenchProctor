# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
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


@app.post("/BenchmarkTest00064")
async def BenchmarkTest00064(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    exec(str(processed))
    return {"updated": True}
