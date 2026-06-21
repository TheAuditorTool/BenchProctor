# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def to_text(value):
    return str(value).strip()

async def BenchmarkTest62402(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
