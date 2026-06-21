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

async def BenchmarkTest49754(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
