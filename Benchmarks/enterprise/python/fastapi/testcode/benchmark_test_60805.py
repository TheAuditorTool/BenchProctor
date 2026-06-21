# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest60805(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    os.remove(str(data))
    return {"updated": True}
