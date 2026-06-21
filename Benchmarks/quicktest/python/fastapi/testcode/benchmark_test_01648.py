# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest01648(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
