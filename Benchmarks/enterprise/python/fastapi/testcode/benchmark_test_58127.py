# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest58127(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    request.session.clear()
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(profile_value), secure=True, httponly=True, samesite='Strict')
    return resp
