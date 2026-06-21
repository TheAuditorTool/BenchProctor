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

async def BenchmarkTest11355(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
