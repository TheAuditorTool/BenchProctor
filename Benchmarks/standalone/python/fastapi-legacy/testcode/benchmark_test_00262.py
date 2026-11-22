# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from starlette.responses import JSONResponse
import os
import hashlib


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00262")
async def BenchmarkTest00262(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % str(raw_body)
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    padder = padding.PKCS7(128).padder()
    padded = padder.update(str(data).encode()) + padder.finalize()
    encryptor = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
