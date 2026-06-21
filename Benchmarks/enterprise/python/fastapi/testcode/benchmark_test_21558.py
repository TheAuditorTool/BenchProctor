# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from Crypto.Cipher import DES
from app_runtime import db


async def BenchmarkTest21558(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(comment_value).encode().ljust(8)[:8])
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
