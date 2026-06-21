# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest75773(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    async def _evasion_task():
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    return await _evasion_task()
