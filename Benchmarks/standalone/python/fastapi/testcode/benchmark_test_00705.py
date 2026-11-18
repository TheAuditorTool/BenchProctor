# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import os
import hashlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00705/{id}")
async def BenchmarkTest00705(request: Request, id: str):
    path_value = id
    data = path_value if path_value else 'default'
    _des_key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()[:8]
    ciphertext = DES.new(_des_key, DES.MODE_ECB).encrypt(pad(str(data).encode(), 8))
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
