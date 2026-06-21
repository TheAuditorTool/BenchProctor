# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest10972(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = str(db_value).replace('\x00', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
