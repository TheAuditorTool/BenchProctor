# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest41769(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}
