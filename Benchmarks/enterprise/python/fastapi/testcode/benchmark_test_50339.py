# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest50339(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(profile_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
