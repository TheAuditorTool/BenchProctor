# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest55956(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
