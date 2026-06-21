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

async def BenchmarkTest11723(request: Request):
    user_id = request.query_params.get('id', '')
    data = handle(user_id)
    processed = data[:64]
    return HTMLResponse('<div>' + str(processed) + '</div>')
