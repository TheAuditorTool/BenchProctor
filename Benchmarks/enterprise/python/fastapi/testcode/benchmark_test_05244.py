# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest05244(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
