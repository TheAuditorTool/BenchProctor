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

async def BenchmarkTest30953(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
