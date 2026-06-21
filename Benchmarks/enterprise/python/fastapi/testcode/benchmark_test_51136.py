# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest51136(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(profile_value), max_age=86400)
    return resp
