# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import pickle


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest32098(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = handle(forwarded_ip)
    if time.time() > 1000000000:
        pickle.loads(data.encode('latin-1'))
    return {"updated": True}
