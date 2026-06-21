# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest39905(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if str(data).endswith(('/public', '/static', '/.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
