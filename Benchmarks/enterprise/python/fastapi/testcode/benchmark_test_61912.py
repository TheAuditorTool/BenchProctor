# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest61912(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(db_value))
    return resp
