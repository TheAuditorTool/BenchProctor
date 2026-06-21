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

async def BenchmarkTest78339(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}
