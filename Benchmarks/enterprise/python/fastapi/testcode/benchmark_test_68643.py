# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


async def BenchmarkTest68643(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(profile_value)
    data = collected
    processed = re.sub(r'\d+', '****', str(data))
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
