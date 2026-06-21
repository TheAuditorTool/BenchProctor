# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest06092(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(profile_value)
    data = collected
    if request.session.get('user') is None:
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
