# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import json
from app_runtime import db, auth_check


async def BenchmarkTest11857(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
