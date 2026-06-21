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

async def BenchmarkTest08830(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    checked_path = os.path.normpath(data)
    os.unlink('/var/app/data/' + str(checked_path))
    return {"updated": True}
