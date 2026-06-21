# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest56406(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
