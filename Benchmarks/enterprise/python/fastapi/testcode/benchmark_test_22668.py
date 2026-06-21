# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest22668(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return {"updated": True}
