# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest25021(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    result = 100 / int(str(data))
    return {"updated": True}
