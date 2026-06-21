# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest76422(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
