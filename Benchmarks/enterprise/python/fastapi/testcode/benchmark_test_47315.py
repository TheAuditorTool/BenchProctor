# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


async def BenchmarkTest47315(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = json.loads(profile_value).get('value', profile_value)
    except (json.JSONDecodeError, AttributeError):
        data = profile_value
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
