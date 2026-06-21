# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest15164(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    result = 100 / int(str(data))
    return {"updated": True}
