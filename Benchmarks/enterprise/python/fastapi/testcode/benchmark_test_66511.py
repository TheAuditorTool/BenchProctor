# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest66511(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
