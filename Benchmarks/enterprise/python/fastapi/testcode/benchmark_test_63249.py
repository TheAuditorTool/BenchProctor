# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest63249(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return {"updated": True}
