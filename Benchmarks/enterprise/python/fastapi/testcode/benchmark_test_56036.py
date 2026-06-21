# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest56036(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    request.session['data'] = str(data)
    return {"updated": True}
