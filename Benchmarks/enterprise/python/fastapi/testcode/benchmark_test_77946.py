# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import base64
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest77946(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
