# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from starlette.responses import JSONResponse
import os
import hashlib
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00182")
async def BenchmarkTest00182(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    algorithm = algorithms.ARC4(key)
    encryptor = Cipher(algorithm, mode=None).encryptor()
    ciphertext = encryptor.update(str(data).encode()) + encryptor.finalize()
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
