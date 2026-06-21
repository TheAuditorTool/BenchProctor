# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest03850(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return {"updated": True}
