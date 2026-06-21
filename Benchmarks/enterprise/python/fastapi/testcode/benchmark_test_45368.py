# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest45368(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
