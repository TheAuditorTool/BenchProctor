# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest09635(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
