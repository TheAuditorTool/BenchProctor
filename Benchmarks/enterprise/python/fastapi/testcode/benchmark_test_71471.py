# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest71471(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    os.remove(str(data))
    return {"updated": True}
