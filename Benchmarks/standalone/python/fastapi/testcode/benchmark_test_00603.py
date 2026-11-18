# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from cryptography.fernet import Fernet
import base64
from starlette.responses import JSONResponse
import os


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00603")
async def BenchmarkTest00603(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
