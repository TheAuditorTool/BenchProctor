# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db, auth_check


async def BenchmarkTest23701(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(db_value)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
