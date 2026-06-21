# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest53079(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
