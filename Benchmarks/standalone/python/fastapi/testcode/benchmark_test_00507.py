# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from cryptography.fernet import Fernet
import os
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


@app.post("/BenchmarkTest00507")
async def BenchmarkTest00507(request: Request):
    env_value = os.environ.get('APP_INPUT', '')
    parts = str(env_value).split(',')
    data = ' '.join(parts)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
