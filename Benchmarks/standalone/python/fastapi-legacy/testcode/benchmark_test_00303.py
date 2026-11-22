# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import os
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


@app.post("/BenchmarkTest00303")
async def BenchmarkTest00303(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
