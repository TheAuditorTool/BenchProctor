# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest43058(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
