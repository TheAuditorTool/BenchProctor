# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest17753(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    if str(data).endswith(('/public', '/static', '/.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
