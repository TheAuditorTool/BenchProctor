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

async def BenchmarkTest27488(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}
