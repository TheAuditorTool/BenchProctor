# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest15831(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
