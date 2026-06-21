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

async def BenchmarkTest01307(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
