# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import base64
import socket
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


@app.post("/BenchmarkTest00618")
async def BenchmarkTest00618(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
