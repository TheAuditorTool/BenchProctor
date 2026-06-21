# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import base64
from starlette.responses import JSONResponse
import os
from app_runtime import db


async def BenchmarkTest59132(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
