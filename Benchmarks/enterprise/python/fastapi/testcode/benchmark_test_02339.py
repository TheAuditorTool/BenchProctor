# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest02339(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    requests.get(str(processed))
    return {"updated": True}
