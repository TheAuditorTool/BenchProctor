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

async def BenchmarkTest19993(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    def _primary():
        return HTMLResponse('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
