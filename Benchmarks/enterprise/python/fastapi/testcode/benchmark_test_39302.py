# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest39302(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    async def _evasion_task():
        eval(str(data))
    await _evasion_task()
    return {"updated": True}
