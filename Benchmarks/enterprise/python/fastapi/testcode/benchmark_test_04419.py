# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest04419(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    await _evasion_task()
    return {"updated": True}
