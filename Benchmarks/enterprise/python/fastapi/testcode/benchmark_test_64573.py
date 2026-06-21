# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest64573(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    if time.time() > 1000000000:
        return HTMLResponse('<img src="' + str(data) + '">')
    return {"updated": True}
