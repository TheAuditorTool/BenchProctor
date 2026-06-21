# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest05659(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JSONResponse({'length': len(ciphertext)}, status_code=200)
