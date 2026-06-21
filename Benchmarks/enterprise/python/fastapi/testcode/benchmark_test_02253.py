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

async def BenchmarkTest02253(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}
