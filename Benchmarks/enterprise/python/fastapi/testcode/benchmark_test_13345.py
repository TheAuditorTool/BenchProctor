# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import importlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest13345(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return {"updated": True}
