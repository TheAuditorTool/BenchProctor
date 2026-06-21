# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest07207(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return {"updated": True}
