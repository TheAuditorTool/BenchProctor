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

async def BenchmarkTest51298(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    return HTMLResponse(str(data))
