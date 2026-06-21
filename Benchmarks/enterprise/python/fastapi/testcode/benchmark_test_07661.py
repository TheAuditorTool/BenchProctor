# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db, auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest07661(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
