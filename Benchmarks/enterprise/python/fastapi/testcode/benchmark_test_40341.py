# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from app_runtime import db


async def BenchmarkTest40341(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(db_value).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
