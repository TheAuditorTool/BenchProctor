# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
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


@app.post("/BenchmarkTest00084")
async def BenchmarkTest00084(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ' '.join(parts)
    requests.get(str(data))
    return {"updated": True}
