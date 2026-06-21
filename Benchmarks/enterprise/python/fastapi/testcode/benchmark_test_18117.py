# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import re
from starlette.responses import JSONResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest18117(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
