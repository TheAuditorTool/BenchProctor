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

async def BenchmarkTest75796(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
