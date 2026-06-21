# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest56882(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    prefix = ''
    data = prefix + str(profile_value)
    request.session.clear()
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
