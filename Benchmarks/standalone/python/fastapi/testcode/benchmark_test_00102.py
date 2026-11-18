# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import json


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00102")
async def BenchmarkTest00102(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body!s}'
    parsed = json.loads(data)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
