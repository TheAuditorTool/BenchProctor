# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest56095(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
