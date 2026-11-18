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


@app.post("/BenchmarkTest00327")
async def BenchmarkTest00327(request: Request):
    auth_header = request.headers.get('authorization', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(auth_header))
    os.unlink(checked_path)
    return {"updated": True}
