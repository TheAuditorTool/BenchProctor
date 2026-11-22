# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from cryptography.hazmat.decrepit.ciphers.algorithms import ARC4
from cryptography.hazmat.primitives.ciphers import Cipher
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


@app.post("/BenchmarkTest00241")
async def BenchmarkTest00241(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    algorithm = ARC4(key)
    encryptor = Cipher(algorithm, mode=None).encryptor()
    ciphertext = encryptor.update(str(data).encode()) + encryptor.finalize()
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
