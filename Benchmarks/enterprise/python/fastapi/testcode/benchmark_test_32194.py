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

async def BenchmarkTest32194(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
