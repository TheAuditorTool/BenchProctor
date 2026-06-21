# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest12264(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
