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

async def BenchmarkTest71624(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    if time.time() > 1000000000:
        return HTMLResponse('<img src="' + str(data) + '">')
    return {"updated": True}
