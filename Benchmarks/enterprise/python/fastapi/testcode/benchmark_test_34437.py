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

async def BenchmarkTest34437(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
