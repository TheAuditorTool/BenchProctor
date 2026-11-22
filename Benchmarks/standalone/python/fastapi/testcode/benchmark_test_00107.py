# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
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


@app.post("/BenchmarkTest00107")
async def BenchmarkTest00107(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ' '.join(str(forwarded_ip).split())
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + ChaCha20Poly1305(key).encrypt(nonce, str(data).encode(), None)
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
