# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest40836(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
