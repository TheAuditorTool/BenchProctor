# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest05034(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
