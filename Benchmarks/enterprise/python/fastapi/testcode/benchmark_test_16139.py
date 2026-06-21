# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest16139(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    result = 100 / int(str(data))
    return {"updated": True}
