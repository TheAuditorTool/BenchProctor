# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest51427(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    result = 100 / int(str(data))
    return {"updated": True}
