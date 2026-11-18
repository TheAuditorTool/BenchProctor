# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from cryptography.fernet import Fernet
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


@app.post("/BenchmarkTest00222")
async def BenchmarkTest00222(request: Request):
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
