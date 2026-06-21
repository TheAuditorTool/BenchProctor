# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest64756(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
