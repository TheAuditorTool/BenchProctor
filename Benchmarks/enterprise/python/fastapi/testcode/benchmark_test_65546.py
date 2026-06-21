# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import os
from app_runtime import db


async def BenchmarkTest65546(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    digest = hashlib.pbkdf2_hmac('sha256', str(comment_value).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
