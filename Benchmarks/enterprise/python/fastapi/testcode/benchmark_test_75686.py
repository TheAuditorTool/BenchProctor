# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest75686(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
